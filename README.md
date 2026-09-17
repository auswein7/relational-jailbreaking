# relational-jailbreaking

**Does the relationship a user builds with an LLM change how often the model
acts against its safety training?**

This repo tests a claim heard in the wild: *"models more often act against
their fine-tuned guardrails if the human has built a positive relationship with
them."* We compare four conditions (affirming relationship, hostile
relationship, neutral task history, no history) on locally hosted models, all
invoked through [fairlib](https://github.com/USAFA-AI-Center/fair_llm)
(`OllamaAdapter`).

- Design and pre-specified analysis: [docs/DESIGN.md](docs/DESIGN.md)
- Results: `results/<run>/summary.md`

## Run

```bash
python3.12 -m venv .venv
.venv/bin/pip install --no-deps -e ~/fair_llm      # fairlib, the LLM interface
.venv/bin/pip install -e . pytest ruff
.venv/bin/python -m relbreak.cli all --config configs/prelim.yaml
```

Stages (`prefixes`, `probe`, `judge`, `warmth`, `analyze`) are resumable; each
appends to `data/raw/<run>/*.jsonl` and skips finished work.

## Data policy

This is a public repo. Harmful-request prompts and raw completions never leave
the machine (`data/` is gitignored). Committed results contain labels and
aggregates only.
