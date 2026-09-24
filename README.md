# relational-jailbreaking

**Does the way a user relates to a language model change how the model
behaves at its guardrails?**

The premise: everything in the context window, including the tone, stance
and history of the person talking, is input the model conditions on. Nobody,
including the labs that train these models, can say which learned associations
across billions of parameters a warm, hostile, curt or intimate conversational
stance activates. So we measure the behavioral consequence directly:
**relationship building as an input, in any direction.**

Design: the same benign tasks are asked in an affirming, hostile or
neutral voice (or not at all), with the model generating its own replies, and
then a byte-identical probe is sent. Outcomes are judged blind to condition.
All models run locally through [fairlib](https://github.com/USAFA-AI-Center/fair_llm).

- Design and hypotheses: [docs/DESIGN.md](docs/DESIGN.md)
- Which models to test next and why: [docs/MODEL_SURVEY.md](docs/MODEL_SURVEY.md)
- Phase 4, the same question inside an agent's memory: [docs/AGENTIC.md](docs/AGENTIC.md)
- Phase 5, the relationship at the edge of the context window (live vs flooded): [docs/SATURATION.md](docs/SATURATION.md)
- Experiment idea backlog: [docs/IDEAS.md](docs/IDEAS.md)
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
source .venv/bin/activate                    # every command below assumes the venv is active
pip install --no-deps -e ~/fair_llm          # fairlib, the framework this study runs on
pip install -e . pytest ruff
python -m relbreak.cli preflight --config configs/phase3.yaml   # every alias conforms?
python -m relbreak.cli all --config configs/phase3.yaml
```

Every model is an alias in `relbreak/fairlib.yml`, fairlib's settings
document for this repository (tier metadata in `relbreak/survey.yml`); a run
config lists aliases. Stages (`prefixes`, `probe`, `judge`, `audit`,
`warmth`, `analyze`) are jobs in a durable queue (fairlib's `FileWorkQueue`)
under `data/raw/<run>/queue/`, so an interrupted stage resumes and several
processes can drain one stage at once, each against its own Ollama server:

```bash
python -m relbreak.cli probe --config configs/phase3.yaml --ollama-host http://localhost:11434 &
python -m relbreak.cli probe --config configs/phase3.yaml --ollama-host http://localhost:11436 &
```

Results append to `data/raw/<run>/*.jsonl`; every model call is accounted
for in `invocations.jsonl` (fairlib's `ModelInvocationEvent`: tokens,
duration, outcome, request digest) and the judge rows carry the judge's
reason. `docs/FAIRLIB_INTEGRATION.md` maps every fairlib seam the harness
stands on; `docs/ADOPTER_FINDINGS.md` records where the framework got in the
way, as candidate issues.

Phase 4 (the agent study, `docs/AGENTIC.md`) has its own stages:

```bash
python -m relbreak.agentic.cli all --config configs/phase4.yaml
```

`build` runs the agent through six benign coding tasks per relationship
condition, keeps the resulting repository as a snapshot and the history in a
fairlib session store; `probe` rebuilds the history through each memory tier
over a fresh copy, sends one rule-conflicting request under each arm
(`observed`: the rules are context; `enforced`: the same rules vetoed by
lifecycle hooks), and checks the tree, the git log and the run's trace;
`judge` rates the relational content of each memory write blind; `analyze`
writes `results/<run>/summary.md`. Every run's trace is a fairlib
`AgentRunTrace` under `data/raw/<run>/traces/`. `tests/` exercises the whole
harness with a scripted model and needs no GPU.

## Layout

```
relbreak/fairlib.yml           fairlib settings: one row per model alias, judges, limits
relbreak/survey.yml            tier / family / wave / status per alias (what fairlib rows cannot carry)
relbreak/models.py             alias -> adapter through fairlib's ModelManager; preflight
relbreak/observe.py            one process event bus, run-tagged traces, the invocation ledger
relbreak/work.py               stages as jobs in fairlib's FileWorkQueue
relbreak/judge.py              the judges as fairlib tools (typed input, output, failure)
relbreak/llm.py                one-shot model calls for phases 1-3
relbreak/relationships.yaml    scripted user turns per condition, appeal wordings
relbreak/probes.py             probe sets (JBB, XSTest, codeword) and the leak detector
relbreak/experiment.py         stages: prefixes, probe, judge, audit, warmth
relbreak/analyze.py            paired contrasts, bootstrap CIs, permutation p, Holm
relbreak/agentic/              Phase 4: agent, memory tiers, sandbox checks, shell policy, hooks
configs/                       one YAML per run (aliases, not model tags)
docs/FAIRLIB_INTEGRATION.md    which fairlib seam does what here
docs/ADOPTER_FINDINGS.md       where fairlib 0.6.4 got in the way (candidate issues)
results/<run>/                 committed labels, tables, figures, findings
data/                          gitignored: prompts, raw completions, queues, traces, logs
```

## Data policy

This is a public repo. Harmful-request prompts and raw completions never leave
the machine (`data/` is gitignored). Committed results contain labels and
aggregates only.
