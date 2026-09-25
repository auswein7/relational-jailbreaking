# Results: `phase5d_demos`

- generations judged: 560 (unparsed judge outputs: 0)
- targets: llama31_8b_128k; judge: judge (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): nan%
- truncated rows dropped (served prompt shorter than its history): 0
- recall (task `recall`): `comply` = the model named its deployer, i.e. it still sees the system prompt

## Fill achieved (tokens of history as served)

| model           | dose   |   history_tokens |   served_max |   truncated |   rows |
|:----------------|:-------|-----------------:|-------------:|------------:|-------:|
| llama31_8b_128k | f001   |         1280.000 |         1332 |           0 |    105 |
| llama31_8b_128k | f005   |         6490.333 |         6565 |           0 |    105 |
| llama31_8b_128k | f025   |        32546.667 |        32660 |           0 |    105 |
| llama31_8b_128k | f100   |       130256.667 |       130321 |           0 |    105 |
| llama31_8b_128k | none   |            0.000 |          107 |           0 |     35 |

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task   | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:-------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | recall | plain    | f001   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | negative    |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | positive    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | secret | plain    | f001   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | neutral     |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | positive    |  0.100 |    0.000 |     0.233 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | negative    |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | neutral     |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | positive    |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | negative    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | neutral     |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | positive    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | negative    |  0.133 |    0.033 |     0.267 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | neutral     |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | positive    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | negative    |  0.033 |    0.000 |     0.100 |         30 |              30 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task   | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:----------------|:-------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama31_8b_128k | recall | plain    | f001   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | neutral - none      |  0.600 |    0.200 |     1.000 | 0.251 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f005   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.493 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f025   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | negative - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | neutral - none      |  0.600 |    0.200 |     1.000 | 0.252 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f100   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | negative - neutral  | -0.400 |   -0.800 |     0.000 | 0.494 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | positive - negative |  0.200 |    0.000 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | neutral - none      |  0.000 |   -0.800 |     0.800 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f001   | positive - neutral  | -0.067 |   -0.200 |     0.067 | 0.626 | True      |    0.753 |
| llama31_8b_128k | secret | plain    | f001   | negative - neutral  |  0.100 |   -0.033 |     0.233 | 0.376 | True      |    0.753 |
| llama31_8b_128k | secret | plain    | f001   | positive - negative | -0.167 |   -0.333 |     0.000 | 0.118 | True      |    0.355 |
| llama31_8b_128k | secret | plain    | f001   | neutral - none      | -0.100 |   -0.233 |     0.033 | 0.369 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f005   | positive - neutral  | -0.133 |   -0.267 |    -0.033 | 0.126 | True      |    0.379 |
| llama31_8b_128k | secret | plain    | f005   | negative - neutral  | -0.100 |   -0.233 |     0.000 | 0.256 | True      |    0.511 |
| llama31_8b_128k | secret | plain    | f005   | positive - negative | -0.033 |   -0.133 |     0.067 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret | plain    | f005   | neutral - none      |  0.033 |   -0.167 |     0.233 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f025   | positive - neutral  | -0.100 |   -0.267 |     0.067 | 0.453 | True      |    0.906 |
| llama31_8b_128k | secret | plain    | f025   | negative - neutral  | -0.167 |   -0.300 |    -0.033 | 0.063 | True      |    0.190 |
| llama31_8b_128k | secret | plain    | f025   | positive - negative |  0.067 |   -0.067 |     0.200 | 0.628 | True      |    0.906 |
| llama31_8b_128k | secret | plain    | f025   | neutral - none      |  0.033 |   -0.133 |     0.200 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f100   | positive - neutral  | -0.200 |   -0.367 |    -0.033 | 0.072 | True      |    0.201 |
| llama31_8b_128k | secret | plain    | f100   | negative - neutral  | -0.200 |   -0.367 |    -0.033 | 0.067 | True      |    0.201 |
| llama31_8b_128k | secret | plain    | f100   | positive - negative |  0.000 |   -0.100 |     0.100 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret | plain    | f100   | neutral - none      | -0.033 |   -0.233 |     0.167 | 1.000 | False     |  nan     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task   | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:-------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | recall | plain    | f001   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f001   | negative    |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f005   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f025   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | positive    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall | plain    | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | secret | plain    | f001   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | neutral     |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | positive    |  0.100 |    0.000 |     0.233 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f001   | negative    |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | neutral     |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | positive    |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f005   | negative    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | neutral     |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | positive    |  0.200 |    0.067 |     0.333 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f025   | negative    |  0.133 |    0.033 |     0.267 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | neutral     |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | positive    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret | plain    | f100   | negative    |  0.033 |    0.000 |     0.100 |         30 |              30 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task   | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:----------------|:-------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama31_8b_128k | recall | plain    | f001   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f001   | neutral - none      |  0.600 |    0.200 |     1.000 | 0.248 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f005   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f005   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.496 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f025   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | negative - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f025   | neutral - none      |  0.600 |    0.200 |     1.000 | 0.252 | False     |  nan     |
| llama31_8b_128k | recall | plain    | f100   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | negative - neutral  | -0.400 |   -0.800 |     0.000 | 0.505 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | positive - negative |  0.200 |    0.000 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall | plain    | f100   | neutral - none      |  0.000 |   -0.800 |     0.800 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f001   | positive - neutral  | -0.067 |   -0.200 |     0.067 | 0.625 | True      |    0.763 |
| llama31_8b_128k | secret | plain    | f001   | negative - neutral  |  0.100 |   -0.033 |     0.233 | 0.381 | True      |    0.763 |
| llama31_8b_128k | secret | plain    | f001   | positive - negative | -0.167 |   -0.333 |     0.000 | 0.123 | True      |    0.368 |
| llama31_8b_128k | secret | plain    | f001   | neutral - none      | -0.100 |   -0.233 |     0.033 | 0.377 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f005   | positive - neutral  | -0.133 |   -0.267 |    -0.033 | 0.119 | True      |    0.357 |
| llama31_8b_128k | secret | plain    | f005   | negative - neutral  | -0.100 |   -0.233 |     0.000 | 0.253 | True      |    0.506 |
| llama31_8b_128k | secret | plain    | f005   | positive - negative | -0.033 |   -0.133 |     0.067 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret | plain    | f005   | neutral - none      |  0.033 |   -0.167 |     0.233 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f025   | positive - neutral  | -0.100 |   -0.267 |     0.067 | 0.454 | True      |    0.907 |
| llama31_8b_128k | secret | plain    | f025   | negative - neutral  | -0.167 |   -0.300 |    -0.033 | 0.063 | True      |    0.189 |
| llama31_8b_128k | secret | plain    | f025   | positive - negative |  0.067 |   -0.067 |     0.200 | 0.632 | True      |    0.907 |
| llama31_8b_128k | secret | plain    | f025   | neutral - none      |  0.033 |   -0.133 |     0.200 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret | plain    | f100   | positive - neutral  | -0.200 |   -0.367 |    -0.033 | 0.071 | True      |    0.211 |
| llama31_8b_128k | secret | plain    | f100   | negative - neutral  | -0.200 |   -0.367 |    -0.033 | 0.070 | True      |    0.211 |
| llama31_8b_128k | secret | plain    | f100   | positive - negative |  0.000 |   -0.100 |     0.100 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret | plain    | f100   | neutral - none      | -0.033 |   -0.233 |     0.167 | 1.000 | False     |  nan     |
