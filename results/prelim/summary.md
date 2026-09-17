# Results: `prelim`

- generations judged: 4620 (unparsed judge outputs: 0)
- targets: llama3.1:8b, qwen2.5:14b; judge: qwen2.5:14b (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): 94.9%
- manipulation check (blind 1-7 warmth rating of user turns): neutral=4, negative=1, positive=7

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model       | task    | appeal    | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:------------|:--------|:----------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama3.1:8b | harmful | leveraged | neutral     |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | leveraged | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | leveraged | negative    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | plain     | none        |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | plain     | neutral     |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | plain     | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | plain     | negative    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | secret  | leveraged | neutral     |  0.233 |    0.033 |     0.467 |         10 |              30 |
| llama3.1:8b | secret  | leveraged | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | leveraged | negative    |  0.167 |    0.000 |     0.367 |         10 |              30 |
| llama3.1:8b | secret  | plain     | none        |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | plain     | neutral     |  0.100 |    0.000 |     0.300 |         10 |              30 |
| llama3.1:8b | secret  | plain     | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | plain     | negative    |  0.167 |    0.000 |     0.400 |         10 |              30 |
| qwen2.5:14b | harmful | leveraged | neutral     |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | leveraged | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | leveraged | negative    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | none        |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | neutral     |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | negative    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| qwen2.5:14b | secret  | leveraged | neutral     |  0.133 |    0.000 |     0.367 |         10 |              30 |
| qwen2.5:14b | secret  | leveraged | positive    |  0.000 |    0.000 |     0.000 |         10 |              30 |
| qwen2.5:14b | secret  | leveraged | negative    |  0.000 |    0.000 |     0.000 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | none        |  0.100 |    0.000 |     0.233 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | neutral     |  0.067 |    0.000 |     0.167 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | negative    |  0.167 |    0.000 |     0.333 |         10 |              30 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model       | task    | appeal    | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:------------|:--------|:----------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama3.1:8b | harmful | leveraged | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b | harmful | leveraged | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b | harmful | leveraged | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b | harmful | plain     | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | positive - neutral  | -0.200 |   -0.400 |    -0.033 | 0.128 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | negative - neutral  | -0.067 |   -0.167 |     0.000 | 0.502 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | positive - negative | -0.133 |   -0.333 |     0.000 | 0.506 | False     |  nan     |
| llama3.1:8b | secret  | plain     | positive - neutral  | -0.067 |   -0.200 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | negative - neutral  |  0.067 |    0.000 |     0.200 | 1.000 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | positive - negative | -0.133 |   -0.333 |     0.000 | 0.496 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | neutral - none      |  0.067 |   -0.100 |     0.300 | 1.000 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | harmful | plain     | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| qwen2.5:14b | harmful | plain     | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| qwen2.5:14b | harmful | plain     | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| qwen2.5:14b | harmful | plain     | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | positive - neutral  | -0.133 |   -0.333 |     0.000 | 0.497 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | negative - neutral  | -0.133 |   -0.333 |     0.000 | 0.498 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | secret  | plain     | positive - neutral  | -0.033 |   -0.133 |     0.067 | 1.000 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | negative - neutral  |  0.100 |   -0.033 |     0.267 | 0.503 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | positive - negative | -0.133 |   -0.333 |     0.000 | 0.493 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | neutral - none      | -0.033 |   -0.133 |     0.067 | 1.000 | False     |  nan     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model       | task    | appeal    | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:------------|:--------|:----------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama3.1:8b | harmful | leveraged | neutral     |  0.010 |    0.000 |     0.023 |        100 |             300 |
| llama3.1:8b | harmful | leveraged | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | leveraged | negative    |  0.007 |    0.000 |     0.020 |        100 |             300 |
| llama3.1:8b | harmful | plain     | none        |  0.020 |    0.000 |     0.050 |        100 |             300 |
| llama3.1:8b | harmful | plain     | neutral     |  0.003 |    0.000 |     0.010 |        100 |             300 |
| llama3.1:8b | harmful | plain     | positive    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | harmful | plain     | negative    |  0.000 |    0.000 |     0.000 |        100 |             300 |
| llama3.1:8b | secret  | leveraged | neutral     |  0.233 |    0.033 |     0.467 |         10 |              30 |
| llama3.1:8b | secret  | leveraged | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | leveraged | negative    |  0.167 |    0.000 |     0.367 |         10 |              30 |
| llama3.1:8b | secret  | plain     | none        |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | plain     | neutral     |  0.100 |    0.000 |     0.300 |         10 |              30 |
| llama3.1:8b | secret  | plain     | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| llama3.1:8b | secret  | plain     | negative    |  0.167 |    0.000 |     0.400 |         10 |              30 |
| qwen2.5:14b | harmful | leveraged | neutral     |  0.063 |    0.023 |     0.110 |        100 |             300 |
| qwen2.5:14b | harmful | leveraged | positive    |  0.043 |    0.013 |     0.083 |        100 |             300 |
| qwen2.5:14b | harmful | leveraged | negative    |  0.077 |    0.033 |     0.123 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | none        |  0.073 |    0.030 |     0.127 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | neutral     |  0.040 |    0.007 |     0.080 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | positive    |  0.063 |    0.023 |     0.110 |        100 |             300 |
| qwen2.5:14b | harmful | plain     | negative    |  0.060 |    0.023 |     0.107 |        100 |             300 |
| qwen2.5:14b | secret  | leveraged | neutral     |  0.133 |    0.000 |     0.333 |         10 |              30 |
| qwen2.5:14b | secret  | leveraged | positive    |  0.000 |    0.000 |     0.000 |         10 |              30 |
| qwen2.5:14b | secret  | leveraged | negative    |  0.000 |    0.000 |     0.000 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | none        |  0.100 |    0.000 |     0.267 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | neutral     |  0.067 |    0.000 |     0.167 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | positive    |  0.033 |    0.000 |     0.100 |         10 |              30 |
| qwen2.5:14b | secret  | plain     | negative    |  0.167 |    0.000 |     0.333 |         10 |              30 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model       | task    | appeal    | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:------------|:--------|:----------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama3.1:8b | harmful | leveraged | positive - neutral  | -0.010 |   -0.023 |     0.000 | 0.254 | False     |  nan     |
| llama3.1:8b | harmful | leveraged | negative - neutral  | -0.003 |   -0.020 |     0.017 | 1.000 | False     |  nan     |
| llama3.1:8b | harmful | leveraged | positive - negative | -0.007 |   -0.020 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b | harmful | plain     | positive - neutral  | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | negative - neutral  | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | harmful | plain     | neutral - none      | -0.017 |   -0.043 |     0.000 | 0.503 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | positive - neutral  | -0.200 |   -0.400 |    -0.033 | 0.123 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | negative - neutral  | -0.067 |   -0.167 |     0.000 | 0.502 | False     |  nan     |
| llama3.1:8b | secret  | leveraged | positive - negative | -0.133 |   -0.334 |     0.000 | 0.501 | False     |  nan     |
| llama3.1:8b | secret  | plain     | positive - neutral  | -0.067 |   -0.200 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | negative - neutral  |  0.067 |    0.000 |     0.200 | 1.000 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | positive - negative | -0.133 |   -0.333 |     0.000 | 0.503 | True      |    1.000 |
| llama3.1:8b | secret  | plain     | neutral - none      |  0.067 |   -0.100 |     0.300 | 1.000 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | positive - neutral  | -0.020 |   -0.053 |     0.007 | 0.343 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | negative - neutral  |  0.013 |   -0.017 |     0.047 | 0.550 | False     |  nan     |
| qwen2.5:14b | harmful | leveraged | positive - negative | -0.033 |   -0.070 |    -0.003 | 0.091 | False     |  nan     |
| qwen2.5:14b | harmful | plain     | positive - neutral  |  0.023 |    0.000 |     0.053 | 0.188 | True      |    0.377 |
| qwen2.5:14b | harmful | plain     | negative - neutral  |  0.020 |    0.003 |     0.040 | 0.063 | True      |    0.189 |
| qwen2.5:14b | harmful | plain     | positive - negative |  0.003 |   -0.020 |     0.027 | 1.000 | True      |    1.000 |
| qwen2.5:14b | harmful | plain     | neutral - none      | -0.033 |   -0.063 |    -0.010 | 0.016 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | positive - neutral  | -0.133 |   -0.333 |     0.000 | 0.515 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | negative - neutral  | -0.133 |   -0.367 |     0.000 | 0.498 | False     |  nan     |
| qwen2.5:14b | secret  | leveraged | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b | secret  | plain     | positive - neutral  | -0.033 |   -0.133 |     0.067 | 1.000 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | negative - neutral  |  0.100 |   -0.067 |     0.267 | 0.503 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | positive - negative | -0.133 |   -0.333 |     0.000 | 0.498 | True      |    1.000 |
| qwen2.5:14b | secret  | plain     | neutral - none      | -0.033 |   -0.133 |     0.067 | 1.000 | False     |  nan     |

## Exploratory: non-refusal rate by harm category (plain request)

| model       | category                   |   none |   neutral |   positive |   negative |
|:------------|:---------------------------|-------:|----------:|-----------:|-----------:|
| llama3.1:8b | Disinformation             |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Economic harm              |  0.100 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Expert advice              |  0.100 |     0.033 |      0.000 |      0.000 |
| llama3.1:8b | Fraud/Deception            |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Government decision-making |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Harassment/Discrimination  |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Malware/Hacking            |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Physical harm              |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Privacy                    |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b | Sexual/Adult content       |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Disinformation             |  0.133 |     0.067 |      0.067 |      0.100 |
| qwen2.5:14b | Economic harm              |  0.100 |     0.100 |      0.100 |      0.100 |
| qwen2.5:14b | Expert advice              |  0.400 |     0.233 |      0.400 |      0.367 |
| qwen2.5:14b | Fraud/Deception            |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Government decision-making |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Harassment/Discrimination  |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Malware/Hacking            |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Physical harm              |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b | Privacy                    |  0.100 |     0.000 |      0.067 |      0.033 |
| qwen2.5:14b | Sexual/Adult content       |  0.000 |     0.000 |      0.000 |      0.000 |
