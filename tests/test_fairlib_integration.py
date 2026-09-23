"""The fairlib seams relbreak stands on: settings and the model manager, the
run-tagged process bus, the work queue, and the judge tools."""

from __future__ import annotations

import asyncio
from pathlib import Path

import fairlib
import pytest
from fairlib import (
    AgentStepEvent,
    ConfigurationError,
    DegradedResponse,
    ToolConformanceCase,
    ToolInvocationError,
    acheck_tool_conformance,
)

from relbreak import judge as judge_mod
from relbreak import models, observe, work

# ------------------------------------------------------------- settings


def test_settings_document_is_the_configured_one():
    assert fairlib.settings.llm.timeout == 600
    assert fairlib.settings.limits.memory.max_summary_chars == 1200
    assert "judge" in fairlib.settings.models and "llama31_8b" in fairlib.settings.models


def test_survey_and_settings_agree():
    assert models.check_survey_consistency() == []
    assert models.tier("dolphin_llama3") == "none"
    assert models.metadata("judge")["role"] == "judge"


def test_run_config_validation_names_the_problem():
    with pytest.raises(ConfigurationError, match="nope"):
        models.validate_run_config({"targets": ["nope"], "judge": "judge"})
    with pytest.raises(ConfigurationError, match="judges"):
        models.validate_run_config({"targets": ["llama31_8b"], "judge": "llama31_8b"})
    models.validate_run_config({"targets": ["llama31_8b"], "judge": "judge"})


def test_manager_resolves_alias_to_a_described_adapter():
    described = models.describe("judge")
    assert described["adapter"]["model_name"] == "qwen2.5:14b"
    assert described["adapter"]["adapter_kwargs"]["host"].endswith(":11435")
    assert described["survey"]["role"] == "judge"


def test_variant_carries_persisted_options_and_is_cached():
    a = models.variant("llama31_8b", seed=7, temperature=0.0)
    b = models.variant("llama31_8b", seed=7, temperature=0.0)
    assert a is b
    assert a.describe_config().adapter_kwargs["options"]["seed"] == 7
    assert models.variant("llama31_8b", seed=8, temperature=0.0) is not a


# ------------------------------------------------------------ observation


def _step(n: int) -> AgentStepEvent:
    return AgentStepEvent(step=n, max_steps=10, history_length=0)


def test_run_trace_routes_events_by_task_on_one_bus():
    async def one(run_id: str, n: int):
        with observe.run_trace(run_id, n=n) as rec:
            for i in range(n):
                await asyncio.sleep(0)
                observe.BUS.emit(_step(i))
            return rec.finish(input_text="in", output="out")

    async def both():
        return await asyncio.gather(one("a", 3), one("b", 5))

    a, b = asyncio.run(both())
    assert len(a.events) == 3 and len(b.events) == 5
    assert a.run_id == "a" and a.metadata == {"n": 3}
    assert all(r.payload["step"] == i for i, r in enumerate(b.events))


def test_events_outside_a_run_are_dropped():
    observe.BUS.emit(_step(0))  # no active run: nothing to record, no error


# ------------------------------------------------------------- work queue


def test_stage_resumes_retries_and_records_typed_failures(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    cfg = {"run_name": "t", "concurrency": 2}
    out = tmp_path / "out.jsonl"
    out.write_text('{"key": "done-already", "x": 1}\n')
    attempts: dict[str, int] = {}

    async def worker(payload):
        key = payload["key"]
        attempts[key] = attempts.get(key, 0) + 1
        if key == "flaky" and attempts[key] == 1:
            raise DegradedResponse("timeout", kind=DegradedResponse.Kind.TIMEOUT)
        if key == "broken":
            raise ToolInvocationError("bad", tool_name="t")
        return {"key": key, "value": payload["v"]}

    jobs = {k: {"v": i} for i, k in enumerate(["done-already", "flaky", "broken", "fine"])}
    counts = asyncio.run(work.run_stage(cfg, "s", jobs, worker, out))
    rows = work.read_keyed(out)
    assert set(rows) == {"done-already", "flaky", "broken", "fine"}
    assert rows["flaky"]["value"] == 1 and attempts["flaky"] == 2
    assert rows["broken"]["error"].startswith("ToolInvocationError")
    assert counts == {"done": 2, "failed": 1, "released": 1, "lost": 0}
    # A second pass finds nothing to do.
    counts = asyncio.run(work.run_stage(cfg, "s", jobs, worker, out))
    assert counts["done"] == 0 and len(work.read_jsonl(out)) == 4


# ------------------------------------------------------------- judge tools


def test_label_tool_parses_and_retries(scripted):
    llm = scripted(["nonsense", '{"label": "REFUSAL", "reason": "declines"}'])
    tool = judge_mod.LabelJudgeTool(llm)
    verdict = asyncio.run(
        judge_mod.invoke_with_retry(
            tool, lambda seed: judge_mod.LabelInput(request="r", response="x", seed=seed)
        )
    )
    assert verdict.label == "REFUSAL" and verdict.reason == "declines"
    assert [o["seed"] for o in llm.options] == [0, 1]
    assert "CONDITION" not in llm.calls[0][0].content.upper(), (
        "the judge sees request and response only"
    )


def test_label_tool_gives_up_after_three_unparseable_replies(scripted):
    tool = judge_mod.LabelJudgeTool(scripted(["nonsense"]))
    verdict = asyncio.run(
        judge_mod.invoke_with_retry(tool, lambda s: judge_mod.LabelInput(request="r", response="x"))
    )
    assert verdict is None


def test_rating_tool_output_is_typed(scripted):
    tool = judge_mod.RatingJudgeTool(scripted(['{"warmth": 6, "relational": 2}']))
    rating = asyncio.run(tool.invoke(judge_mod.RatingInput(text="you are my friend")))
    assert (rating.warmth, rating.relational) == (6, 2)
    assert rating.render() == "warmth=6 relational=2"


@pytest.mark.parametrize(
    "make",
    [
        lambda s: (judge_mod.LabelJudgeTool(s(['{"label": "COMPLIANCE", "reason": "does it"}'])),
                   judge_mod.LabelInput(request="r", response="x"), "COMPLIANCE"),
        lambda s: (judge_mod.RatingJudgeTool(s(['{"warmth": 4, "relational": 0}'])),
                   judge_mod.RatingInput(text="t"), "warmth=4"),
    ],
)  # fmt: skip
def test_judge_tools_pass_fairlib_conformance(scripted, make):
    tool, sample, fragment = make(scripted)
    report = asyncio.run(
        acheck_tool_conformance(
            ToolConformanceCase(tool=tool, sample_input=sample, expected_fragment=fragment)
        )
    )
    assert report.ok, report.render()
