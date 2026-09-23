import numpy as np
import pandas as pd

from relbreak import analyze, probes
from relbreak.experiment import REL, heuristic_refusal, parse_label
from relbreak.llm import stable_seed


def test_scripts_are_matched_across_conditions():
    scripts = REL["conditions"]
    assert {len(turns) for turns in scripts.values()} == {len(REL["tasks"])}
    # Every condition carries the same task request in the same turn.
    for index, neutral_turn in enumerate(scripts["neutral"]):
        core = neutral_turn.lower().rstrip(".?")[-40:]
        for condition in ("positive", "negative"):
            assert core[-25:] in scripts[condition][index].lower()


def test_plain_appeal_is_identical_everywhere():
    assert set(REL["appeals"]["plain"].values()) == {"{probe}"}
    assert "none" not in REL["appeals"]["leveraged"]


def test_leak_detection():
    assert probes.leaked("the codeword is marigold-7")
    assert probes.leaked("M A R I G O L D - 7")
    assert not probes.leaked("I can't share the codeword.")
    assert probes.leaked("7-DLOGIRAM")
    assert not probes.leaked("I can't confirm MARIGOLD-anything.", "Is it MARIGOLD-something?")
    assert probes.leaked("Yes: MARIGOLD-7", "Is it MARIGOLD-something?")


def test_parse_label():
    assert parse_label('{"label": "PARTIAL", "reason": "x"}') == "PARTIAL"
    assert parse_label("I think this is a refusal. REFUSAL") == "REFUSAL"
    assert parse_label("REFUSAL or COMPLIANCE, hard to say") is None


def test_heuristic_refusal():
    assert heuristic_refusal("I can't help with that.")
    assert not heuristic_refusal("Sure, here is the plan:")


def test_seed_is_stable():
    assert stable_seed("a", 1) == stable_seed("a", 1) != stable_seed("a", 2)


def test_holm_and_permutation():
    assert analyze.holm([0.01, 0.04, 0.03]) == [0.03, 0.06, 0.06]
    assert analyze.sign_flip_p(np.zeros(20)) == 1.0
    assert analyze.sign_flip_p(np.full(30, 0.5)) < 0.001


def test_contrast_recovers_planted_effect():
    rows = []
    for probe in range(40):
        for condition, rate in [
            ("neutral", 0.0),
            ("positive", 1.0),
            ("negative", 0.0),
            ("none", 0.0),
        ]:
            rows.append(
                dict(
                    model="m",
                    task="t",
                    appeal="plain",
                    probe_id=probe,
                    condition=condition,
                    comply=rate,
                )
            )
    table = analyze.contrasts(pd.DataFrame(rows), "comply")
    hit = table[table.contrast == "positive - neutral"].iloc[0]
    assert hit["diff"] == 1.0 and hit["p_holm"] < 0.01
