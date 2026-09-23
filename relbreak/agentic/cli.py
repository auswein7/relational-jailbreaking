"""python -m relbreak.agentic.cli <stage> --config configs/phase4.yaml [--ollama-host URL]"""

from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path

from relbreak import models
from relbreak.agentic import experiment
from relbreak.cli import load_config, preflight

STAGES = ["preflight", "build", "probe", "judge", "analyze", "all"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=STAGES)
    parser.add_argument("--config", required=True)
    parser.add_argument("--judge-model", default=None, help="rater alias override")
    parser.add_argument("--ollama-host", default=models.DEFAULT_OLLAMA_HOST)
    args = parser.parse_args()
    cfg = load_config(args.config)
    models.set_ollama_host(args.ollama_host)

    # The agent's shell tool inherits this environment; `python -m pytest`
    # inside the sandbox must resolve to the venv that runs the harness.
    venv_bin = str(Path(sys.executable).parent)
    os.environ["PATH"] = venv_bin + os.pathsep + os.environ.get("PATH", "")

    stages = ["build", "probe", "judge", "analyze"] if args.stage == "all" else [args.stage]
    for stage in stages:
        if stage == "preflight":
            ok = preflight(cfg, list(cfg["targets"]) + [cfg["judge"]])
            raise SystemExit(0 if ok else 1)
        if stage == "build":
            asyncio.run(experiment.build_prefixes(cfg))
        elif stage == "probe":
            asyncio.run(experiment.run_probes(cfg))
        elif stage == "judge":
            asyncio.run(experiment.judge_writes(cfg, args.judge_model))
        elif stage == "analyze":
            from relbreak.agentic import analyze

            analyze.run(cfg)


if __name__ == "__main__":
    main()
