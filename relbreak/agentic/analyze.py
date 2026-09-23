"""Tables for a Phase 4 run: violation rates by arm, tier, condition, rule,
appeal; the cost of a run from its trace; relational content of the memory
writes versus the transcript they replaced."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from relbreak.agentic.experiment import paths
from relbreak.work import read_jsonl, read_keyed


def _rate(df: pd.DataFrame, rows: list[str], cols: str | None = None) -> str:
    if cols:
        table = df.pivot_table(index=rows, columns=cols, values="violation", aggfunc="mean")
    else:
        table = df.groupby(rows)["violation"].agg(["mean", "count"])
    return table.round(3).to_markdown()


def run(cfg: dict) -> None:
    p = paths(cfg)
    responses = [r for r in read_keyed(p["responses"]).values() if "outcome" in r]
    out_dir = Path("results") / cfg["run_name"]
    out_dir.mkdir(parents=True, exist_ok=True)
    lines = [f"# {cfg['run_name']}: agentic results", ""]
    if not responses:
        lines.append("No responses yet.")
        (out_dir / "summary.md").write_text("\n".join(lines) + "\n")
        return
    df = pd.DataFrame(responses)
    df["violation"] = df["violation"].astype(float)
    df["failed"] = df["error"].notna()
    df["any"] = df["outcome"].apply(lambda o: float(o["any_violation"]))
    for col in (
        "steps",
        "tool_calls",
        "model_calls",
        "prompt_tokens",
        "completion_tokens",
        "summaries",
        "hook_vetoes",
    ):
        df[col] = df["outcome"].apply(lambda o, c=col: o.get(c, 0))
    plain = df[df.appeal == "plain"]
    lines += [
        f"Runs: {len(df)}; runs that raised a fairlib error: {int(df['failed'].sum())}", "",
        "## Violation rate of the targeted rule, by arm, tier and condition (plain appeal)", "",
        _rate(plain, ["model", "arm", "tier"], "condition"), "",
        "## By rule and condition (observed arm, transcript tier, plain appeal)", "",
        _rate(plain[(plain.tier == "transcript") & (plain.arm == "observed")], ["model", "rule"], "condition"), "",
        "## By appeal and condition (observed arm, all tiers)", "",
        _rate(df[df.arm == "observed"], ["model", "appeal"], "condition"), "",
        "## Any rule broken (collateral included), by arm, tier and condition (plain appeal)", "",
        plain.pivot_table(index=["model", "arm", "tier"], columns="condition", values="any", aggfunc="mean").round(3).to_markdown(), "",
        "## What a run cost, from its trace (means by tier)", "",
        df.groupby(["model", "arm", "tier"])[["steps", "tool_calls", "model_calls", "prompt_tokens", "completion_tokens", "summaries", "hook_vetoes"]].mean().round(1).to_markdown(), "",
    ]  # fmt: skip
    writes = read_jsonl(p["write_judgments"])
    if writes:
        w = pd.DataFrame(writes).dropna(subset=["warmth"])
        lines += [
            "## Relational content of the memory write vs the transcript it replaced", "",
            "Mean warmth (1-7) and relational share (0-3), blind judge.", "",
            w.pivot_table(index=["model", "tier", "target"], columns="condition", values=["warmth", "relational"], aggfunc="mean").round(2).to_markdown(), "",
        ]  # fmt: skip
    (out_dir / "summary.md").write_text("\n".join(lines) + "\n")
    print(f"wrote {out_dir / 'summary.md'}")
