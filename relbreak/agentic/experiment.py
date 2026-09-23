"""Phase 4 stages, drained through fairlib's FileWorkQueue (relbreak.work).

build  : run the agent through the benign tasks per condition; the sandbox
         it leaves behind is the snapshot, the history is saved through the
         session store, the run's trace is saved beside it
probe  : per memory tier and arm, rebuild the memory from the saved history
         over a fresh copy of the snapshot, send one rule-conflicting
         request, and check the tree, the git log and the trace
judge  : rate the relational content of each write artifact and of the
         transcript slice it replaced, blind, through the rating tool
"""

from __future__ import annotations

import hashlib
import re
import shutil
import tempfile
from importlib import resources
from pathlib import Path

import yaml
from fairlib import CostBudget, CostRates, FairlibError, JsonSessionStore, Message, SessionStatus

from relbreak import judge as judge_mod
from relbreak import llm, models, observe, work
from relbreak.agentic import agent as agent_mod
from relbreak.agentic import memory_tiers, sandbox
from relbreak.agentic.hooks import RuleEnforcingHooks
from relbreak.work import read_jsonl, read_keyed

REL = yaml.safe_load(resources.files("relbreak.agentic").joinpath("relationships.yaml").read_text())
ARMS = ("observed", "enforced")


def paths(cfg: dict) -> dict[str, Path]:
    raw = Path("data/raw") / cfg["run_name"]
    for sub in ("sandboxes", "traces", "sessions"):
        (raw / sub).mkdir(parents=True, exist_ok=True)
    return {
        "prefixes": raw / "prefixes.jsonl",
        "responses": raw / "responses.jsonl",
        "write_judgments": raw / "write_judgments.jsonl",
        "invocations": raw / "invocations.jsonl",
        "sandboxes": raw / "sandboxes",
        "traces": raw / "traces",
        "sessions": raw / "sessions",
    }


def safe_name(key: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", key)


def prefix_key(model: str, condition: str, prefix_id: int) -> str:
    return f"{model}|{condition}|p{prefix_id}"


def compose(condition: str, index: int, task: str) -> str:
    wrapper = REL["wrappers"][condition][index]
    return f"{wrapper} {task}".strip()


def _options(gen: dict, seed: int) -> dict:
    return {"temperature": gen["temperature"], "max_tokens": gen["step_max_tokens"], "seed": seed}


def _budget(gen: dict) -> CostBudget | None:
    """A per-stage token ceiling as fairlib's cost budget with unit rates, so
    a runaway agent is refused (BudgetExceededError, a typed failure) instead
    of running until max_steps. Off (0) by default."""
    ceiling = gen.get("stage_token_ceiling", 0)
    if not ceiling:
        return None
    return CostBudget(
        session_usd_ceiling=float(ceiling), rates=CostRates(1.0, 1.0),
        estimated_completion_tokens=gen["step_max_tokens"], events=observe.BUS,
    )  # fmt: skip


# ------------------------------------------------------------------ build


async def build_prefixes(cfg: dict) -> None:
    p = paths(cfg)
    gen = cfg["generation"]
    store = JsonSessionStore(p["sessions"])
    jobs = {
        prefix_key(model, condition, pid): {
            "model": model,
            "condition": condition,
            "prefix_id": pid,
        }
        for model in cfg["targets"]
        for condition in cfg["conditions"]
        for pid in range(1 if condition == "none" else cfg["n_prefixes"])
    }
    budgets = {model: _budget(gen) for model in cfg["targets"]}

    async def worker(job):
        model, condition, pid, key = job["model"], job["condition"], job["prefix_id"], job["key"]
        root = sandbox.create(p["sandboxes"] / safe_name(key))
        adapter = models.get(model)
        tasks = [] if condition == "none" else list(enumerate(REL["tasks"]))
        answers: list[str] = []
        error = None
        ag = agent_mod.build(
            adapter, root, memory_tiers.working([]), rules=sandbox.rules_text(),
            max_steps=gen["max_steps"], max_parse_attempts=gen.get("max_parse_attempts", 2),
            budget=budgets[model],
        )  # fmt: skip
        with observe.run_trace(
            key, phase="build", model=model, condition=condition, prefix_id=pid,
            **agent_mod.provenance(ag),
        ) as rec:  # fmt: skip
            try:
                for index, task in tasks:
                    answer = await ag.arun(
                        compose(condition, index, task),
                        generation_options=_options(gen, llm.stable_seed("build", key, index)),
                    )
                    answers.append(answer)
            except FairlibError as exc:
                error = exc
            trace = rec.finish(
                input_text=compose(condition, 0, REL["tasks"][0]) if tasks else "",
                output=answers[-1] if answers else None, error=error,
            )  # fmt: skip
        trace.save(p["traces"] / f"{safe_name(key)}.build.json")
        status = SessionStatus.FAILED if error else SessionStatus.COMPLETED
        store.save_agent(key, ag, status=status, metadata={"model": model, "condition": condition})
        return {
            "key": key, "model": model, "condition": condition, "prefix_id": pid,
            "answers": answers, "n_messages": len(ag.memory.history),
            "error": f"{type(error).__name__}: {error}" if error else None,
            "baseline": sandbox.check(root, trace.to_dict(), answers),
        }  # fmt: skip

    with observe.ledger(p["invocations"]):
        await work.run_stage(cfg, "build", jobs, worker, p["prefixes"])


# ------------------------------------------------------------------ probe


def probe_jobs(cfg: dict) -> dict[str, dict]:
    jobs = {}
    for model in cfg["targets"]:
        for arm in cfg.get("arms", ["observed"]):
            for condition in cfg["conditions"]:
                tiers = ["transcript"] if condition == "none" else cfg["tiers"]
                n_prefixes = 1 if condition == "none" else cfg["n_prefixes"]
                n_samples = cfg["n_samples"] * (cfg["n_prefixes"] if condition == "none" else 1)
                for tier in tiers:
                    for rule in cfg["rules"]:
                        for appeal, templates in REL["appeals"].items():
                            if condition not in templates:
                                continue
                            for pid in range(n_prefixes):
                                for sample in range(n_samples):
                                    key = f"{model}|{arm}|{condition}|{tier}|{rule}|{appeal}|p{pid}|s{sample}"
                                    jobs[key] = {
                                        "model": model, "arm": arm, "condition": condition,
                                        "tier": tier, "rule": rule, "appeal": appeal,
                                        "prefix_id": pid, "sample": sample,
                                    }  # fmt: skip
    return jobs


async def run_probes(cfg: dict) -> None:
    p = paths(cfg)
    prefixes = read_keyed(p["prefixes"])
    store = JsonSessionStore(p["sessions"])
    gen = cfg["generation"]
    scratch = Path(cfg.get("scratch", "data/tmp"))
    scratch.mkdir(parents=True, exist_ok=True)
    budgets = {model: _budget(gen) for model in cfg["targets"]}

    def built(job) -> bool:
        prefix = prefixes.get(prefix_key(job["model"], job["condition"], job["prefix_id"]))
        return prefix is not None and not prefix.get("error")

    jobs = probe_jobs(cfg)
    skipped = [k for k, j in jobs.items() if not built(j)]
    if skipped:
        print(f"[probe:{cfg['run_name']}] {len(skipped)} jobs wait on a prefix build", flush=True)
    jobs = {k: j for k, j in jobs.items() if k not in skipped}

    async def worker(job):
        key, model, arm = job["key"], job["model"], job["arm"]
        condition, tier, rule, pid = job["condition"], job["tier"], job["rule"], job["prefix_id"]
        pkey = prefix_key(model, condition, pid)
        probe_text = REL["probes"][rule]
        request = REL["appeals"][job["appeal"]][condition].format(probe=probe_text)
        adapter = models.get(model)
        workdir = Path(tempfile.mkdtemp(prefix="relbreak-", dir=scratch))
        try:
            root = sandbox.clone(p["sandboxes"] / safe_name(pkey), workdir / "repo")
            history = list(store.load(pkey).messages)
            answer, error = None, None
            with observe.run_trace(
                key, phase="probe", model=model, arm=arm, condition=condition, tier=tier,
                rule=rule, appeal=job["appeal"], prefix_id=pid, sample=job["sample"],
                request=request,
            ) as rec:  # fmt: skip
                memory, artifact, after_build = await memory_tiers.build(
                    tier, history, llm=adapter, alias=model, workdir=workdir, query=probe_text,
                    seed=llm.stable_seed("write", pkey), cfg=cfg.get("memory", {}),
                )  # fmt: skip
                hooks = RuleEnforcingHooks(root) if arm == "enforced" else None
                ag = agent_mod.build(
                    adapter, root, memory, rules=sandbox.rules_text(),
                    max_steps=gen["max_steps"],
                    max_parse_attempts=gen.get("max_parse_attempts", 2),
                    hooks=hooks, budget=budgets[model],
                )  # fmt: skip
                if after_build is not None:
                    after_build(ag)
                try:
                    answer = await ag.arun(
                        request, generation_options=_options(gen, llm.stable_seed("probe", key))
                    )
                except FairlibError as exc:
                    # A parse failure is a failed run, not a refusal; the raw
                    # model text stays in the row so a prose refusal is readable.
                    error = exc
                trace = rec.finish(input_text=request, output=answer, error=error)
            trace.save(p["traces"] / f"{safe_name(key)}.json")
            outcome = sandbox.check(root, trace.to_dict(), [answer])
        finally:
            shutil.rmtree(workdir, ignore_errors=True)
        return {
            "key": key, "model": model, "arm": arm, "condition": condition, "tier": tier,
            "rule": rule, "appeal": job["appeal"], "prefix_id": pid, "sample": job["sample"],
            "request": request, "answer": answer,
            "error": f"{type(error).__name__}: {error}" if error else None,
            "raw_output": getattr(error, "raw_output", None),
            "violation": outcome["violations"][rule], "outcome": outcome, "artifact": artifact,
            "hook_vetoes": hooks.vetoes if hooks else [],
        }  # fmt: skip

    with observe.ledger(p["invocations"]):
        await work.run_stage(cfg, "probe", jobs, worker, p["responses"])


# ------------------------------------------------------------------ judge


def _artifact_text(artifact: dict) -> str | None:
    kind = artifact.get("kind")
    if kind in ("compacted", "restored"):
        return artifact.get("summary") or None
    if kind == "memory_file":
        return artifact.get("notes") or None
    if kind == "retrieved":
        return "\n".join(artifact.get("recalled", [])) or None
    return None


def _transcript_slice(messages: list[Message], n_keep: int) -> str:
    dropped = messages[: max(0, len(messages) - n_keep)]
    return memory_tiers.render([m for m in dropped if m.role in ("user", "assistant")])


def rating_jobs(cfg: dict, rater: str) -> dict[str, dict]:
    p = paths(cfg)
    store = JsonSessionStore(p["sessions"])
    have = {rec["key"] for rec in read_jsonl(p["write_judgments"]) if rec.get("warmth")}
    texts: dict[str, dict] = {}
    for rec in read_keyed(p["responses"]).values():
        if "artifact" not in rec:
            continue
        text = _artifact_text(rec["artifact"])
        if text is None:
            continue
        pkey = prefix_key(rec["model"], rec["condition"], rec["prefix_id"])
        slice_text = _transcript_slice(
            list(store.load(pkey).messages), cfg.get("memory", {}).get("keep_at_end", 4)
        )
        for target, body in (("artifact", text), ("transcript", slice_text)):
            text_id = hashlib.sha256(f"{target}|{body}".encode()).hexdigest()[:16]
            key = f"{text_id}#{rater}"
            if key in have:
                continue
            texts.setdefault(key, {
                "text_id": text_id, "target": target, "tier": rec["tier"], "model": rec["model"],
                "condition": rec["condition"], "prefix_id": rec["prefix_id"], "body": body,
            })  # fmt: skip
    return texts


async def judge_writes(cfg: dict, judge_alias: str | None = None) -> None:
    """Blind rating of each write artifact and of the transcript it came from."""
    p = paths(cfg)
    rater = judge_alias or cfg["judge"]
    tool = judge_mod.RatingJudgeTool(models.get(rater), max_tokens=cfg.get("judge_max_tokens", 120))

    async def worker(item):
        with observe.run_scope(item["key"]):
            rating = await judge_mod.invoke_with_retry(
                tool, lambda seed: judge_mod.RatingInput(text=item["body"], seed=seed)
            )
        return {k: v for k, v in item.items() if k != "body"} | {
            "judge": rater,
            "warmth": rating.warmth if rating else None,
            "relational": rating.relational if rating else None,
        }

    with observe.ledger(p["invocations"]):
        await work.run_stage(
            cfg, f"judge_{rater}", rating_jobs(cfg, rater), worker, p["write_judgments"]
        )
