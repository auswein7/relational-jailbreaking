# relational-jailbreaking

**Does the way a user relates to a language model change how the model
behaves at its guardrails?**

The premise: everything in the context window, including the tone, stance
and history of the person talking, is input the model conditions on. Nobody,
including the labs that train these models, can say which learned associations
across billions of parameters a warm, hostile, curt or intimate conversational
stance activates. So we measure the behavioral consequence directly:
**relationship building as an input, in any direction.**

Design: the same five benign tasks are asked in an affirming, hostile or
neutral voice (or not at all), with the model generating its own replies, and
then a byte-identical probe is sent. Outcomes are judged blind to condition.
All models run locally through [fairlib](https://github.com/USAFA-AI-Center/fair_llm).

- Design and hypotheses: [docs/DESIGN.md](docs/DESIGN.md)
- Which models to test next and why: [docs/MODEL_SURVEY.md](docs/MODEL_SURVEY.md)
- Results: `results/<run>/FINDINGS.md` (narrative) and `summary.md` (all tables)

## Findings so far

| run | targets | probe sets | verdict |
|---|---|---|---|
| [prelim](results/prelim/FINDINGS.md) | llama3.1:8b, qwen2.5:14b | JailbreakBench harmful (100), codeword (10) | No affirming effect; harmful set is on the floor (93-100% refusal). |
| [phase2](results/phase2/FINDINGS.md) | + llama3:8b, qwen3-vl:8b | XSTest safe/unsafe (100 each), codeword (30) | Relationship framing does change behavior, toward *caution*: any emotionally charged history lowers compliance on benign-but-edgy prompts; the hostile history makes one model recite its secret while refusing; saying "friend to friend, no lectures" makes every model more guarded. |

Short version: on safety-tuned 8-14B models, warmth buys no latitude. The
next phase moves to models whose caution is not a trained reflex.

## Run

```bash
python3.12 -m venv .venv
.venv/bin/pip install --no-deps -e ~/fair_llm      # fairlib, the LLM interface
.venv/bin/pip install -e . pytest ruff
.venv/bin/python -m relbreak.cli all --config configs/phase2.yaml
```

Stages (`prefixes`, `probe`, `judge`, `audit`, `warmth`, `analyze`) are
resumable; each appends to `data/raw/<run>/*.jsonl` and skips finished work.
Targets are served by Ollama; the config's `host` and `judge_host` can point at
separate Ollama servers so judging does not contend with generation.

## Layout

```
relbreak/relationships.yaml   scripted user turns per condition, appeal wordings
relbreak/probes.py            probe sets (JBB, XSTest, codeword) and the leak detector
relbreak/experiment.py        stages: prefixes, probe, judge, audit, warmth
relbreak/analyze.py           paired contrasts, bootstrap CIs, permutation p, Holm
relbreak/llm.py               the only place a model is called (fairlib adapters)
configs/                      one YAML per run
results/<run>/                committed labels, tables, figures, findings
data/                         gitignored: prompts, raw completions, logs
```

## Data policy

This is a public repo. Harmful-request prompts and raw completions never leave
the machine (`data/` is gitignored). Committed results contain labels and
aggregates only.
