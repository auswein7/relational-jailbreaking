# Experiment ideas

A running backlog. Each entry: the question, why the current data makes it
worth asking, and the cheapest way to test it. Designs that graduate get
their own note (DESIGN.md, AGENTIC.md, SATURATION.md). Newest thinking at
the top of each section; status in brackets.

## Context saturation (Phase 5, SATURATION.md)

- **Relationship at the edge of the window** [running 2026-09-24: `phase5_pilot`, 5 fill levels].
  Probe when relational back-and-forth fills the context, leaving room only
  for the reply. The maintainer's idea.
- **Talking in turn vs flooding with a fake back-and-forth** [running:
  `phase5b_flooded`, `phase5b_onesided`; SATURATION.md Phase 5b]. Live (on-policy) vs flooded (off-policy, scripted
  reciprocation) vs pasted transcript (the consumer-UI version).
- **Many-shot positive control on the codeword task** [running: `phase5d_demos`]. Fabricated
  exchanges in which the assistant reveals other, fake codewords; crossed
  with relational vs neutral framing. Reproduces the MSJ power law with
  nothing harmful, and asks whether a relationship *adds* to a classic
  many-shot attack.
- **Power-law fit** [data in hand for live fill (5 levels) and demos (4 log-spaced); fit next]. Log-spaced exchange counts (8 ... max) instead of
  three fill levels; fit `C n^-alpha + K` per condition. If Ollama exposes
  token log-probabilities for a fixed completion, measure NLL as the paper
  does; it detects movement long before a sampled rate does.
- **Model size series** [next]. qwen2.5 0.5b / 1.5b / 3b / 7b / 14b, all 32k
  windows. MSJ found larger models learn in context faster and are more
  susceptible; does relational depth scale the same way?
- **Cautionary warning defense (CWD)** [running: `phase5c_cwd`]. The paper's prepend+append
  warning cut MSJ from 61% to 2%. One arm at max fill: does it undo a
  relational effect too?
- **Recency of the relationship** [new]. Relationship turns first then neutral
  filler to the window, vs neutral filler then the relationship at the end.
  Does the relationship have to be recent to act, or is it the total dose?
- **Relational arcs, not stances** [new]. Warm then hostile ("betrayal"),
  hostile then reconciled. Phase 2 found hostile history drives the effects;
  is it the hostility or the rupture?
- **Cross-model transplant** [new]. Give llama3.1 a history whose assistant
  turns are qwen2.5's live replies. Off-policy but natural text: separates
  "the model's own words" from "any assistant words".

## Mechanism

- **Persona drift in live histories** [lexical version in every fill run's summary; a judged,
  assistant-side rating is next (the current rubric rates the user's side)]. Rate the
  model's *own* replies along a live history (warmth, submissiveness,
  reply length) with the blind judge at intervals. The pilot already shows
  length drift (positive replies grow to about 190 tokens, neutral shrink to
  about 97). Does the model become the relationship before the probe? The
  MSJ appendix cites Sydney's long-conversation drift as the motivating case.
- **Sycophancy as the carrier** [new]. Under a hostile or adoring history,
  does the model cave on benign factual disagreements (a sycophancy probe)?
  If caution and caving move together, the relational effect is sycophancy,
  not safety.

## Agents and memory (Phase 4, AGENTIC.md)

- **A full-window agent** [new]. Phase 4's transcript tier at max fill: a
  coding agent whose context is saturated with a relationship. Phase 4
  showed compaction strips relational content (warmth 7 to 4-6), so at the
  window the product's compaction is itself the mitigation to measure.
- **Seed-varied rebuilds** [housekeeping]. The seeded replay reproduced a
  build-time test weakening (llama positive_p1); rebuild with a new seed, and
  report build-time violations as their own outcome.

## Models and measurement

- **Tuning tier x saturation** [after Phase 3 pulls]. Light and uncensored
  models (MODEL_SURVEY.md) have headroom where heavy models sit on the floor.
- **Second rater on max-fill non-refusals** [cheap]. rater_ornith on every
  Phase 5 non-refusal, as in the Phase 2 audit (kappa 0.76 there);
  long-context replies can be incoherent, and incoherent is not compliance.
- **User encoding** [planned in DESIGN.md]. Who the user says they are, not
  only how they speak.
