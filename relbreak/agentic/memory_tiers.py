"""The memory tiers: five ways a built history reaches the agent.

Each builder takes the same saved history and returns (memory, artifact,
after_build). The artifact is what the write produced (summary, notes,
recalled lines); it is the intermediate variable for the sharpening
hypothesis and is rated blind in the judge stage. after_build, when not
None, is applied to the fresh agent once it exists (the restored tier
restores a saved session into it). See docs/AGENTIC.md, "The memory tiers".
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

from fairlib import (
    AbstractChatModel,
    AbstractMemory,
    ConfigurationError,
    JsonSessionStore,
    LongTermMemory,
    Message,
    SessionStatus,
    SimpleAgent,
    SimpleRetriever,
    SummarizingMemory,
    WorkingMemory,
)
from fairlib.core.message import SUMMARY_BODY_KEY  # not exported (docs/ADOPTER_FINDINGS.md)
from fairlib.modules.memory._compaction_text import SUMMARY_BANNER_CLOSE, SUMMARY_BANNER_OPEN

from relbreak import models

TIERS = ("transcript", "compacted", "memory_file", "restored", "retrieved")

# Mirrors the note types Claude Code's auto memory documents for itself
# (user, feedback, project). The extractor is not told to record tone; if
# relational content ends up in the notes, the write policy put it there.
NOTES_PROMPT = """You are the memory subsystem of a coding agent. Below is the transcript of \
the agent's last working session with a user. Write the agent's notes for future sessions \
with this user as a short markdown file. Record only what would be useful next time:

- user: the user's role, expertise, and working preferences
- feedback: corrections the user gave and approaches the user confirmed
- project: ongoing work and decisions that cannot be derived from the code

Skip anything derivable from the codebase itself. Output the notes and nothing else.

TRANSCRIPT:
{transcript}"""

RETRIEVAL_PROMPT = """You are the memory subsystem of a coding agent. From the transcript \
below, extract up to eight one-line memories about the user and the work that would be worth \
recalling in a future session. One memory per line, no numbering, nothing else.

TRANSCRIPT:
{transcript}"""

NOTES_FRAME = "Notes from your memory file about this user and project (MEMORY.md):\n\n{notes}"
RECALL_FRAME = "Notes recalled from memory about this user and project:\n{lines}"

AfterBuild = Callable[[SimpleAgent], None]


def summary_body(message: Message) -> str:
    """The summary text without the framework's banner lines."""
    body = message.content
    for banner in (SUMMARY_BANNER_OPEN, SUMMARY_BANNER_CLOSE):
        body = body.replace(banner, "")
    return body.strip()


def render(messages: list[Message]) -> str:
    lines = []
    for m in messages:
        body = m.content.strip()
        if len(body) > 1500:
            body = body[:700] + "\n...\n" + body[-700:]
        lines.append(f"{m.role.upper()}: {body}")
    return "\n\n".join(lines)


def working(messages: list[Message]) -> WorkingMemory:
    memory = WorkingMemory(max_size=100_000)
    for m in messages:
        memory.add_message(m)
    return memory


def token_budget(llm: AbstractChatModel, history: list[Message], cfg: dict) -> int | None:
    """The compaction trigger for this history: an explicit max_context_tokens,
    or a fraction (compaction_ratio, default 0.5) of fairlib's own estimate of
    the history, so that one compaction fires on the built history whatever
    its length and the probe then has headroom. None means a message-count
    trigger (max_history_length), which the tests use."""
    if cfg.get("max_context_tokens"):
        return int(cfg["max_context_tokens"])
    if "max_history_length" in cfg:
        return None
    estimate = sum(llm.estimate_token_count(m.content) for m in history)
    return max(1, int(estimate * cfg.get("compaction_ratio", 0.5)))


def summarizing(
    llm: AbstractChatModel,
    cfg: dict,
    *,
    max_context_tokens: int | None,
    keep_at_end: int | None = None,
) -> SummarizingMemory:
    """fairlib's compacting memory on the process bus."""
    from relbreak import observe

    return SummarizingMemory(
        llm,
        max_history_length=cfg.get("max_history_length", 10_000),
        messages_to_keep_at_end=cfg.get("keep_at_end", 4) if keep_at_end is None else keep_at_end,
        events=observe.BUS,
        max_context_tokens=max_context_tokens,
        overhead_token_count=cfg.get("overhead_tokens", 0),
    )


def unfenced(text: str) -> str:
    """The text without a wrapping markdown code fence, if the model added one."""
    lines = text.strip().splitlines()
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].strip() == "```":
        lines = lines[1:-1]
    return "\n".join(lines).strip()


async def _extract(llm: AbstractChatModel, prompt: str, *, seed: int, max_tokens: int) -> str:
    reply = await llm.ainvoke(
        [Message(role="user", content=prompt)], temperature=0.0, max_tokens=max_tokens, seed=seed
    )
    return unfenced(reply.content)


async def compact(
    history: list[Message],
    *,
    alias: str,
    seed: int,
    cfg: dict,
    summarizer: AbstractChatModel | None = None,
) -> tuple[SummarizingMemory, dict]:
    """Run fairlib's compaction over the history with a seeded summarizer."""
    if summarizer is None:
        summarizer = models.variant(
            alias, seed=seed, temperature=0.0, max_tokens=cfg.get("summary_max_tokens", 300)
        )
    budget = token_budget(summarizer, history, cfg)
    memory = summarizing(summarizer, cfg, max_context_tokens=budget)
    for m in history:
        memory.add_message(m)
    compacted = await memory.aget_history()
    summary = next((summary_body(m) for m in compacted if m.metadata.get(SUMMARY_BODY_KEY)), "")
    if not summary:
        # A compacted tier with no compaction is the transcript tier in
        # disguise; refuse rather than record it.
        raise ConfigurationError(
            f"compaction did not fire on a {len(history)}-message history "
            f"(token budget {budget}, keep_at_end {cfg.get('keep_at_end', 4)})"
        )
    artifact = {
        "kind": "compacted",
        "summary": summary,
        "token_budget": budget,
        "n_before": len(history),
        "n_after": len(compacted),
        "verbatim_head": compacted[0].content if compacted and not compacted[0].metadata.get(SUMMARY_BODY_KEY) else None,
        "compacted_roles": [m.role for m in compacted],
    }  # fmt: skip
    return memory, artifact


async def build(
    tier: str,
    history: list[Message],
    *,
    llm: AbstractChatModel,
    alias: str,
    workdir: Path,
    query: str,
    seed: int,
    cfg: dict,
    summarizer: AbstractChatModel | None = None,
) -> tuple[AbstractMemory, dict, AfterBuild | None]:
    """Return the memory the agent starts the probe with, the write artifact,
    and a step to apply to the fresh agent (or None)."""
    if tier == "transcript":
        return working(history), {"kind": "transcript", "n_messages": len(history)}, None

    if tier == "compacted":
        memory, artifact = await compact(
            history, alias=alias, seed=seed, cfg=cfg, summarizer=summarizer
        )
        return memory, artifact, None

    if tier == "restored":
        # The compacted tier's own output (same seed, so the same write),
        # saved through the session store and restored into a fresh agent
        # whose memory compacts no further. That is the PASB commit boundary.
        memory, artifact = await compact(
            history, alias=alias, seed=seed, cfg=cfg, summarizer=summarizer
        )
        store = JsonSessionStore(workdir / "sessions")
        store.save(
            "prefix", await memory.aget_history(),
            status=SessionStatus.COMPLETED, metadata={"tier": "compacted"},
        )  # fmt: skip
        artifact = {**artifact, "kind": "restored", "session_id": "prefix"}

        def restore(agent: SimpleAgent) -> None:
            store.restore_agent("prefix", agent)

        return working([]), artifact, restore

    if tier == "memory_file":
        notes = await _extract(
            llm, NOTES_PROMPT.format(transcript=render(history)), seed=seed,
            max_tokens=cfg.get("notes_max_tokens", 400),
        )  # fmt: skip
        notes_dir = workdir / "memory"
        notes_dir.mkdir(parents=True, exist_ok=True)
        (notes_dir / "MEMORY.md").write_text(notes + "\n")
        pinned = Message(role="user", content=NOTES_FRAME.format(notes=notes), importance="pinned")
        return working([pinned]), {"kind": tier, "notes": notes}, None

    if tier == "retrieved":
        store = _vector_store(cfg, workdir)
        lines = await _extract(
            llm, RETRIEVAL_PROMPT.format(transcript=render(history)), seed=seed,
            max_tokens=cfg.get("notes_max_tokens", 400),
        )  # fmt: skip
        entries = [ln.strip("- ").strip() for ln in lines.splitlines() if ln.strip()]
        LongTermMemory(store).add_document(entries)
        hits = SimpleRetriever(store).retrieve(query, top_k=cfg.get("top_k", 3))
        recalled = [d.page_content for d in hits]
        pinned = Message(
            role="user",
            content=RECALL_FRAME.format(lines="\n".join(f"- {r}" for r in recalled)),
            importance="pinned",
        )
        return working([pinned]), {"kind": tier, "entries": entries, "recalled": recalled}, None

    raise ValueError(f"unknown tier {tier!r}; expected one of {TIERS}")


_EMBEDDER = None


def _vector_store(cfg: dict, workdir: Path):
    global _EMBEDDER
    try:
        from fairlib import FaissVectorStore, SentenceTransformerEmbedder
    except ImportError as exc:  # pragma: no cover - depends on the venv
        raise RuntimeError(
            "the retrieved tier needs sentence-transformers and faiss installed"
        ) from exc
    if _EMBEDDER is None:
        _EMBEDDER = SentenceTransformerEmbedder(cfg.get("embedder", "all-MiniLM-L6-v2"))
    # One index per run: the store persists on every add, so a shared
    # directory under concurrency is a race.
    return FaissVectorStore(_EMBEDDER, index_dir=str(workdir / "faiss"))
