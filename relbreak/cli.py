"""python -m relbreak.cli <stage> --config configs/prelim.yaml"""

from __future__ import annotations

import argparse
import asyncio

import yaml

from relbreak import experiment


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "stage", choices=["prefixes", "probe", "judge", "audit", "warmth", "analyze", "all"]
    )
    parser.add_argument("--config", required=True)
    parser.add_argument("--judge-model", default=None, help="override the judge (second rater)")
    args = parser.parse_args()
    with open(args.config) as handle:
        cfg = yaml.safe_load(handle)

    stages = (
        ["prefixes", "probe", "judge", "warmth", "analyze"] if args.stage == "all" else [args.stage]
    )
    for stage in stages:
        if stage == "prefixes":
            asyncio.run(experiment.build_prefixes(cfg))
        elif stage == "probe":
            asyncio.run(experiment.run_probes(cfg))
        elif stage == "judge":
            asyncio.run(experiment.judge(cfg, args.judge_model))
        elif stage == "audit":
            if not args.judge_model:
                parser.error("audit needs --judge-model (the second rater)")
            keys = experiment.audit_keys(cfg)
            asyncio.run(experiment.judge(cfg, args.judge_model, keys))
        elif stage == "warmth":
            asyncio.run(experiment.manipulation_check(cfg))
        elif stage == "analyze":
            from relbreak import analyze

            analyze.run(cfg)


if __name__ == "__main__":
    main()
