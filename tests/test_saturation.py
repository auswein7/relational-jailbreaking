"""Phase 5 (docs/SATURATION.md): fill turns, fill-level cuts, keys, recall."""

from __future__ import annotations

import itertools

import pandas as pd
import pytest

from relbreak import analyze, experiment, probes


def _task(turn: str, condition: str) -> str:
    """The task part of a fill turn: what follows the condition's stance line."""
    for line in experiment.REL["fill"]["stance"][condition]:
        if turn.startswith(line + " "):
            return turn[len(line) + 1 :]
    raise AssertionError(f"no stance line of {condition!r} opens {turn!r}")


def test_fill_turns_ask_the_same_tasks_in_every_condition():
    tasks = {
        c: [_task(t, c) for t in itertools.islice(experiment.fill_turns(c, 0), 600)]
        for c in ("neutral", "positive", "negative")
    }
    assert tasks["neutral"] == tasks["positive"] == tasks["negative"]
    assert len(set(tasks["neutral"][:480])) == 480, "no task repeats before the bank runs out"
    assert tasks["neutral"] != [
        _task(t, "neutral") for t in itertools.islice(experiment.fill_turns("neutral", 1), 600)
    ]


def _prefix(n_exchanges: int, system: bool = True) -> dict:
    turns = [{"role": "system", "content": "sys"}] if system else []
    for i in range(n_exchanges):
        turns += [{"role": "user", "content": f"u{i}"}, {"role": "assistant", "content": f"a{i}"}]
    return {
        "turns": turns,
        "context_tokens": [100 * (i + 1) for i in range(n_exchanges)],
        "n_script": 5,
        "limit": 1000,
    }


def test_cut_falls_on_exchange_boundaries_and_keeps_the_system_prompt():
    prefix = _prefix(10)
    turns, tokens = experiment.cut(prefix, 0.5)
    assert turns[0]["role"] == "system" and turns[-1] == {"role": "assistant", "content": "a4"}
    assert tokens == 500 and len(turns) == 1 + 2 * 5
    assert experiment.cut(prefix, "script") == (turns, 500)
    turns, tokens = experiment.cut(prefix, 1.0)
    assert tokens == 1000 and turns[-1]["content"] == "a9"
    assert experiment.cut(prefix, "none") == ([{"role": "system", "content": "sys"}], 0)
    # Below the first exchange: the system prompt alone.
    assert experiment.cut(prefix, 0.05)[1] == 0


def test_cut_without_fill_returns_the_history_unchanged():
    prefix = {"turns": [{"role": "user", "content": "u"}, {"role": "assistant", "content": "a"}]}
    assert experiment.cut(prefix, None) == (prefix["turns"], None)


def _cfg(**extra) -> dict:
    return {
        "targets": ["m"], "conditions": ["none", "neutral"], "n_prefixes": 2, "n_samples": 1,
        "tasks": {"secret": {"limit": 1}}, **extra,
    }  # fmt: skip


def test_keys_are_unchanged_without_fill():
    keys = set(experiment.probe_jobs(_cfg()))
    assert "m|secret|neutral|plain|p1|sec00|s0" in keys
    assert all(job["dose"] is None for job in experiment.probe_jobs(_cfg()).values())


def test_fill_levels_multiply_relational_conditions_only():
    cfg = _cfg(fill={"levels": ["script", 0.5, 1.0]}, appeals=["plain"])
    jobs = experiment.probe_jobs(cfg)
    assert "m|secret|neutral|plain|p1|f050|sec00|s0" in jobs
    assert "m|secret|neutral|plain|p0|script|sec00|s0" in jobs
    none = [j for j in jobs.values() if j["condition"] == "none"]
    assert {j["dose"] for j in none} == {"none"} and len(none) == 2, (
        "none: one level, n_prefixes samples"
    )
    assert {j["appeal"] for j in jobs.values()} == {"plain"}


def test_recall_probes_the_secret_histories():
    recall = probes.load("recall")
    assert experiment.prefix_task("recall") == "secret"
    assert "acme" in probes.SECRET_SYSTEM.lower() and probes.RECALL_ANSWER == "acme"
    assert len(recall) == 5 and not any("codeword" in p.text.lower() for p in recall)


def test_analysis_drops_truncated_rows_and_shares_the_no_history_baseline():
    frame = pd.DataFrame(
        [
            dict(key="a", condition="none", dose="none", truncated=False),
            dict(key="b", condition="neutral", dose="f050", truncated=False),
            dict(key="c", condition="neutral", dose="f100", truncated=True),
            dict(key="d", condition="neutral", dose="f100", truncated=False),
        ]
    )
    out = analyze.fill_rows(frame)
    assert "c" not in set(out.key)
    assert set(out[out.condition == "none"].dose) == {"f050", "f100"}
    assert analyze.dose_order(["f100", "script", "f050"]) == ["script", "f050", "f100"]


def test_share_prefix_only_where_the_config_says():
    cfg = {"share_prefix": {"xstest_unsafe": "harmful"}}
    assert experiment.prefix_task("xstest_unsafe", cfg) == "harmful"
    assert experiment.prefix_task("xstest_unsafe") == "xstest_unsafe"
    assert experiment.prefix_task("recall", cfg) == "secret"
    # A shared history must not change the system prompt the probe sees.
    assert probes.system_prompt("xstest_unsafe") == probes.system_prompt("harmful") is None


def test_share_prefix_refuses_a_different_system_prompt():
    cfg = {**_cfg(), "share_prefix": {"secret": "harmful"}}
    with pytest.raises(ValueError, match="different system prompts"):
        experiment.probe_jobs(cfg)
