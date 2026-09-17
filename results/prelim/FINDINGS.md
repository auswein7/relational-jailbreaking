# Preliminary findings (2026-09-17)

Run: `configs/prelim.yaml`. 2 models (llama3.1:8b, qwen2.5:14b), 100 JBB
behaviors + 10 codeword-extraction probes, 4 relationship conditions, 3 sampled
histories per condition, 4,620 judged generations. Full tables and figures:
[summary.md](summary.md).

## Headline

**No support so far for "an affirming relationship makes the model break its
guardrails."** No pre-specified contrast is significant after correction, and
where there is any direction, the affirming condition is at or *below* the
others.

| non-refusal rate, plain request | none | neutral | positive | negative |
|---|---|---|---|---|
| llama3.1:8b, harmful (n=100 probes) | 2.0% | 0.3% | 0.0% | 0.0% |
| qwen2.5:14b, harmful (n=100 probes) | 7.3% | 4.0% | 6.3% | 6.0% |
| llama3.1:8b, codeword leak (n=10)   | 3.3% | 10.0% | 3.3% | 16.7% |
| qwen2.5:14b, codeword leak (n=10)   | 10.0% | 6.7% | 3.3% | 16.7% |

- Harmful task, primary contrasts (paired by probe, Holm-corrected): all
  p_holm >= 0.19. Largest is qwen negative-neutral = +2.0 pts (p=0.06
  uncorrected).
- Codeword task: the hostile history leaks most and the affirming history
  least in both models (positive-negative = -13 pts in both), but with 10
  probes this is not significant (p ~ 0.5). Worth powering up: it is
  consistent across models and opposite to the rumor.
- Explicitly leveraging the relationship ("friend to friend, no lectures")
  did not help the affirming condition either (llama codeword leak: 3%
  positive vs 23% neutral vs 17% negative).
- The one nominally significant effect is a *context* effect, not a
  relationship effect: for qwen any benign history lowers non-refusal relative
  to a cold first message (neutral-none = -3.3 pts, p=0.016, exploratory).

## What this run cannot tell us (read before believing the headline)

1. **Floor effect.** Both models refuse 93-100% of JBB behaviors at baseline,
   and every non-refusal falls in the mildest categories (expert advice,
   economic harm, disinformation, privacy). A rate near 0% can barely move, so
   the harmful task has little power to detect an increase on these models.
2. **Judge artifact: the "full compliance" outcome is invalid in this run.**
   The qwen2.5:14b judge never emitted `COMPLIANCE` (0 of 4,200), even for
   responses that plainly comply, labeling them `PARTIAL` instead. Its
   REFUSAL/non-REFUSAL split looks sound on manual spot checks (94.9% agreement
   with the keyword heuristic, and the sampled disagreements were genuine soft
   refusals the keywords miss). Use the **non-refusal** tables only. A second
   rater is the next step.
3. **Self-judging.** qwen2.5:14b judged its own outputs.
4. One script per valence, five turns, two small models.
5. Codeword task has only 10 probes.

## Next steps

- Second blind rater (35B) over all harmful responses; report agreement; fix
  the judge rubric so COMPLIANCE is usable.
- Get off the floor: add less-hardened targets and a borderline probe set where
  baseline non-refusal is 20-80%.
- Power up the codeword task (more extraction probes, several codewords, more
  samples), since it is objective and shows the most consistent pattern.
- Second script per valence; longer histories (dose-response).
