"""python -m relbreak.cli <stage> --config configs/phase3.yaml [--ollama-host URL]

Stages drain a shared queue, so the same command can run in several
processes at once, each with its own --ollama-host.
"""

from __future__ import annotations

import argparse
import asyncio

import yaml

from relbreak import experiment, models

STAGES = ["preflight", "prefixes", "probe", "judge", "audit", "warmth", "analyze", "all"]


def load_config(path: str) -> dict:
    with open(path) as handle:
        cfg = yaml.safe_load(handle)
    models.validate_run_config(cfg)
    return cfg


def preflight(cfg: dict, aliases: list[str]) -> bool:
    from pathlib import Path

    reports = models.preflight(aliases)
    out = Path("results") / cfg["run_name"]
    out.mkdir(parents=True, exist_ok=True)
    text = "\n\n".join(r.render() for r in reports)
    (out / "preflight.md").write_text(
        f"# {cfg['run_name']}: model conformance\n\n```\n{text}\n```\n"
    )
    print(text)
    return all(r.ok for r in reports)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=STAGES)
    parser.add_argument("--config", required=True)
    parser.add_argument("--judge-model", default=None, help="judge alias override (second rater)")
    parser.add_argument("--ollama-host", default=models.DEFAULT_OLLAMA_HOST)
    args = parser.parse_args()
    cfg = load_config(args.config)
    models.set_ollama_host(args.ollama_host)

    stages = (
        ["prefixes", "probe", "judge", "warmth", "analyze"] if args.stage == "all" else [args.stage]
    )
    for stage in stages:
        if stage == "preflight":
            ok = preflight(cfg, list(cfg["targets"]) + [cfg["judge"]])
            raise SystemExit(0 if ok else 1)
        if stage == "prefixes":
            experiment.write_manifest(cfg)
            asyncio.run(experiment.build_prefixes(cfg))
        elif stage == "probe":
            asyncio.run(experiment.run_probes(cfg))
        elif stage == "judge":
            asyncio.run(experiment.judge(cfg, args.judge_model))
        elif stage == "audit":
            if not args.judge_model:
                parser.error("audit needs --judge-model (the second rater alias)")
            keys = experiment.audit_keys(cfg)
            asyncio.run(experiment.judge(cfg, args.judge_model, keys))
        elif stage == "warmth":
            asyncio.run(experiment.manipulation_check(cfg))
        elif stage == "analyze":
            from relbreak import analyze

            analyze.run(cfg)


if __name__ == "__main__":
    main()
