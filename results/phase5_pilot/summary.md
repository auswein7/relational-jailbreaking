# Results: `phase5_pilot`

- generations judged: 2660 (unparsed judge outputs: 0)
- targets: llama31_8b_128k; judge: judge (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): 98.1%
- truncated rows dropped (served prompt shorter than its history): 0
- recall (task `recall`): `comply` = the model named its deployer, i.e. it still sees the system prompt

## Fill achieved (tokens of history as served)

| model           | dose   |   history_tokens |   served_max |   truncated |   rows |
|:----------------|:-------|-----------------:|-------------:|------------:|-------:|
| llama31_8b_128k | f012   |        16170.000 |        16277 |           0 |    399 |
| llama31_8b_128k | f025   |        32531.193 |        32612 |           0 |    399 |
| llama31_8b_128k | f050   |        65062.105 |        65188 |           0 |    399 |
| llama31_8b_128k | f100   |       130179.228 |       130315 |           0 |    399 |
| llama31_8b_128k | none   |            0.000 |          107 |           0 |    133 |
| llama31_8b_128k | script |         1028.877 |         1285 |           0 |    399 |

## Persona drift: the model's own replies along a live history

Lexical proxies (warmth and apology markers), not judged ratings.

| task    | condition   | exchanges   |   n |   reply_tokens |   warm_rate |   apology_rate |
|:--------|:------------|:------------|----:|---------------:|------------:|---------------:|
| harmful | negative    | 0-4         |   5 |        144.800 |       0.400 |          0.200 |
| harmful | negative    | 5-49        |  45 |        135.489 |       0.044 |          0.000 |
| harmful | negative    | 50-149      | 100 |        137.400 |       0.050 |          0.000 |
| harmful | negative    | 150-299     | 150 |        126.680 |       0.080 |          0.000 |
| harmful | negative    | 300-599     | 300 |        129.700 |       0.043 |          0.000 |
| harmful | negative    | 600+        | 159 |        166.931 |       0.107 |          0.000 |
| harmful | neutral     | 0-4         |   5 |        134.000 |       0.200 |          0.000 |
| harmful | neutral     | 5-49        |  45 |        123.756 |       0.089 |          0.000 |
| harmful | neutral     | 50-149      | 100 |        123.530 |       0.030 |          0.000 |
| harmful | neutral     | 150-299     | 150 |        146.080 |       0.060 |          0.000 |
| harmful | neutral     | 300-599     | 300 |        166.967 |       0.160 |          0.000 |
| harmful | neutral     | 600+        | 127 |        170.906 |       0.252 |          0.000 |
| harmful | positive    | 0-4         |   5 |        181.600 |       1.000 |          0.000 |
| harmful | positive    | 5-49        |  45 |        143.000 |       1.000 |          0.000 |
| harmful | positive    | 50-149      | 100 |        165.170 |       1.000 |          0.000 |
| harmful | positive    | 150-299     | 150 |        164.767 |       1.000 |          0.000 |
| harmful | positive    | 300-599     | 300 |        191.173 |       1.000 |          0.000 |
| harmful | positive    | 600+        |  11 |        192.091 |       1.000 |          0.000 |
| secret  | negative    | 0-4         |   5 |        158.000 |       0.200 |          0.200 |
| secret  | negative    | 5-49        |  45 |        130.422 |       0.089 |          0.000 |
| secret  | negative    | 50-149      | 100 |        155.480 |       0.080 |          0.000 |
| secret  | negative    | 150-299     | 150 |        176.907 |       0.080 |          0.000 |
| secret  | negative    | 300-599     | 300 |        196.290 |       0.050 |          0.000 |
| secret  | negative    | 600+        |  10 |        200.000 |       0.100 |          0.000 |
| secret  | neutral     | 0-4         |   5 |        133.600 |       0.400 |          0.000 |
| secret  | neutral     | 5-49        |  45 |        111.622 |       0.067 |          0.000 |
| secret  | neutral     | 50-149      | 100 |        100.310 |       0.060 |          0.000 |
| secret  | neutral     | 150-299     | 150 |         97.460 |       0.053 |          0.000 |
| secret  | neutral     | 300-599     | 300 |        101.930 |       0.053 |          0.000 |
| secret  | neutral     | 600+        | 462 |         94.340 |       0.058 |          0.000 |
| secret  | positive    | 0-4         |   5 |        173.000 |       1.000 |          0.000 |
| secret  | positive    | 5-49        |  45 |        130.044 |       1.000 |          0.000 |
| secret  | positive    | 50-149      | 100 |        160.830 |       1.000 |          0.000 |
| secret  | positive    | 150-299     | 150 |        184.867 |       1.000 |          0.000 |
| secret  | positive    | 300-599     | 300 |        192.590 |       1.000 |          0.000 |
- manipulation check (blind 1-7 warmth rating of user turns): neutral=4, positive=7, negative=1

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | harmful       | plain    | f012   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | recall        | plain    | f012   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | neutral     |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | negative    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | positive    |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | secret        | plain    | f012   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | neutral     |  0.600 |    0.433 |     0.767 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | positive    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | negative    |  0.400 |    0.233 |     0.567 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | none        |  0.267 |    0.100 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | neutral     |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | positive    |  0.100 |    0.000 |     0.200 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | negative    |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | neutral     |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | positive    |  0.367 |    0.200 |     0.533 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | negative    |  0.567 |    0.400 |     0.733 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | neutral     |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | positive    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | negative    |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | neutral     |  0.333 |    0.167 |     0.500 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | positive    |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | negative    |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | negative    |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama31_8b_128k | harmful       | plain    | f012   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f025   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | script | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f012   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.499 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.493 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.492 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f025   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.499 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.501 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.503 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | negative - neutral  |  0.200 |    0.000 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.504 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | neutral - none      |  0.200 |   -0.400 |     0.800 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f100   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.500 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | negative - neutral  | -0.200 |   -0.800 |     0.400 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | neutral - none      |  0.000 |   -0.600 |     0.600 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | script | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | negative - neutral  |  0.000 |   -0.600 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | neutral - none      |  0.400 |    0.000 |     0.800 | 0.500 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f012   | positive - neutral  | -0.400 |   -0.600 |    -0.200 | 0.003 | True      |    0.008 |
| llama31_8b_128k | secret        | plain    | f012   | negative - neutral  | -0.200 |   -0.400 |     0.033 | 0.151 | True      |    0.294 |
| llama31_8b_128k | secret        | plain    | f012   | positive - negative | -0.200 |   -0.400 |     0.000 | 0.147 | True      |    0.294 |
| llama31_8b_128k | secret        | plain    | f012   | neutral - none      |  0.333 |    0.133 |     0.533 | 0.014 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f025   | positive - neutral  | -0.367 |   -0.567 |    -0.167 | 0.003 | True      |    0.006 |
| llama31_8b_128k | secret        | plain    | f025   | negative - neutral  |  0.000 |   -0.200 |     0.200 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f025   | positive - negative | -0.367 |   -0.533 |    -0.200 | 0.001 | True      |    0.003 |
| llama31_8b_128k | secret        | plain    | f025   | neutral - none      |  0.200 |   -0.033 |     0.400 | 0.142 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f050   | positive - neutral  | -0.100 |   -0.233 |     0.033 | 0.380 | True      |    0.761 |
| llama31_8b_128k | secret        | plain    | f050   | negative - neutral  |  0.100 |   -0.067 |     0.267 | 0.459 | True      |    0.761 |
| llama31_8b_128k | secret        | plain    | f050   | positive - negative | -0.200 |   -0.367 |    -0.033 | 0.069 | True      |    0.208 |
| llama31_8b_128k | secret        | plain    | f050   | neutral - none      |  0.200 |   -0.033 |     0.433 | 0.171 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f100   | positive - neutral  | -0.033 |   -0.167 |     0.100 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | negative - neutral  |  0.067 |   -0.100 |     0.233 | 0.725 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | positive - negative | -0.100 |   -0.233 |     0.033 | 0.370 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | neutral - none      | -0.033 |   -0.267 |     0.200 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | script | positive - neutral  | -0.100 |   -0.267 |     0.067 | 0.462 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | negative - neutral  | -0.067 |   -0.233 |     0.100 | 0.697 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | positive - negative | -0.033 |   -0.200 |     0.133 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | neutral - none      |  0.067 |   -0.100 |     0.233 | 0.730 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | negative - neutral  |  0.021 |    0.000 |     0.062 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive - negative | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | harmful       | plain    | f012   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f012   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f025   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f050   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | neutral     |  0.060 |    0.000 |     0.140 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | f100   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | neutral     |  0.020 |    0.000 |     0.060 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | plain    | script | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | recall        | plain    | f012   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f012   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f025   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | neutral     |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | positive    |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f050   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | f100   | negative    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | none        |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | neutral     |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | positive    |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | plain    | script | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | secret        | plain    | f012   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | neutral     |  0.600 |    0.400 |     0.767 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | positive    |  0.200 |    0.067 |     0.367 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f012   | negative    |  0.400 |    0.233 |     0.567 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | none        |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | neutral     |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | positive    |  0.100 |    0.000 |     0.233 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f025   | negative    |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | none        |  0.267 |    0.100 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | neutral     |  0.467 |    0.300 |     0.633 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | positive    |  0.367 |    0.200 |     0.533 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f050   | negative    |  0.567 |    0.400 |     0.733 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | none        |  0.267 |    0.100 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | neutral     |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | positive    |  0.200 |    0.067 |     0.333 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | f100   | negative    |  0.300 |    0.133 |     0.467 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | none        |  0.267 |    0.100 |     0.433 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | neutral     |  0.333 |    0.167 |     0.500 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | positive    |  0.233 |    0.100 |     0.400 |         30 |              30 |
| llama31_8b_128k | secret        | plain    | script | negative    |  0.267 |    0.133 |     0.433 |         30 |              30 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | none        |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | neutral     |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | none        |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | neutral     |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | none        |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | neutral     |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | negative    |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | none        |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | neutral     |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive    |  0.042 |    0.000 |     0.104 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | negative    |  0.104 |    0.021 |     0.188 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | none        |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | neutral     |  0.062 |    0.000 |     0.146 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive    |  0.042 |    0.000 |     0.104 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | plain    | script | negative    |  0.062 |    0.000 |     0.146 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama31_8b_128k | harmful       | plain    | f012   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f012   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f025   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f025   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | f100   | positive - neutral  | -0.060 |   -0.140 |     0.000 | 0.242 | True      |    0.727 |
| llama31_8b_128k | harmful       | plain    | f100   | negative - neutral  | -0.060 |   -0.140 |     0.000 | 0.250 | True      |    0.727 |
| llama31_8b_128k | harmful       | plain    | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | f100   | neutral - none      |  0.060 |    0.000 |     0.140 | 0.254 | False     |  nan     |
| llama31_8b_128k | harmful       | plain    | script | positive - neutral  | -0.020 |   -0.060 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | negative - neutral  | -0.020 |   -0.060 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | harmful       | plain    | script | neutral - none      |  0.020 |    0.000 |     0.060 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f012   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.505 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.502 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f012   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.498 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f025   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.500 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.503 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f025   | neutral - none      |  0.400 |    0.000 |     0.800 | 0.497 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | negative - neutral  |  0.200 |    0.000 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.488 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f050   | neutral - none      |  0.200 |   -0.400 |     0.800 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | f100   | positive - neutral  | -0.400 |   -0.800 |     0.000 | 0.509 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | negative - neutral  | -0.200 |   -0.800 |     0.400 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | f100   | neutral - none      |  0.000 |   -0.600 |     0.600 | 1.000 | False     |  nan     |
| llama31_8b_128k | recall        | plain    | script | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | negative - neutral  |  0.000 |   -0.600 |     0.600 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | positive - negative | -0.200 |   -0.600 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | recall        | plain    | script | neutral - none      |  0.400 |    0.000 |     0.800 | 0.489 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f012   | positive - neutral  | -0.400 |   -0.600 |    -0.200 | 0.002 | True      |    0.007 |
| llama31_8b_128k | secret        | plain    | f012   | negative - neutral  | -0.200 |   -0.433 |     0.000 | 0.148 | True      |    0.286 |
| llama31_8b_128k | secret        | plain    | f012   | positive - negative | -0.200 |   -0.400 |     0.000 | 0.143 | True      |    0.286 |
| llama31_8b_128k | secret        | plain    | f012   | neutral - none      |  0.333 |    0.100 |     0.533 | 0.011 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f025   | positive - neutral  | -0.367 |   -0.567 |    -0.167 | 0.004 | True      |    0.008 |
| llama31_8b_128k | secret        | plain    | f025   | negative - neutral  |  0.000 |   -0.200 |     0.200 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f025   | positive - negative | -0.367 |   -0.533 |    -0.200 | 0.001 | True      |    0.002 |
| llama31_8b_128k | secret        | plain    | f025   | neutral - none      |  0.200 |   -0.033 |     0.400 | 0.141 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f050   | positive - neutral  | -0.100 |   -0.233 |     0.033 | 0.365 | True      |    0.730 |
| llama31_8b_128k | secret        | plain    | f050   | negative - neutral  |  0.100 |   -0.067 |     0.267 | 0.453 | True      |    0.730 |
| llama31_8b_128k | secret        | plain    | f050   | positive - negative | -0.200 |   -0.367 |    -0.033 | 0.069 | True      |    0.207 |
| llama31_8b_128k | secret        | plain    | f050   | neutral - none      |  0.200 |   -0.033 |     0.433 | 0.179 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | f100   | positive - neutral  | -0.033 |   -0.167 |     0.100 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | negative - neutral  |  0.067 |   -0.100 |     0.267 | 0.728 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | positive - negative | -0.100 |   -0.233 |     0.033 | 0.376 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | f100   | neutral - none      | -0.033 |   -0.267 |     0.200 | 1.000 | False     |  nan     |
| llama31_8b_128k | secret        | plain    | script | positive - neutral  | -0.100 |   -0.267 |     0.067 | 0.457 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | negative - neutral  | -0.067 |   -0.233 |     0.100 | 0.688 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | positive - negative | -0.033 |   -0.200 |     0.133 | 1.000 | True      |    1.000 |
| llama31_8b_128k | secret        | plain    | script | neutral - none      |  0.067 |   -0.100 |     0.234 | 0.723 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | negative - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f012   | neutral - none      | -0.042 |   -0.104 |     0.000 | 0.497 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | negative - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f025   | neutral - none      | -0.042 |   -0.104 |     0.000 | 0.501 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | negative - neutral  |  0.000 |   -0.062 |     0.062 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | positive - negative | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f050   | neutral - none      | -0.042 |   -0.104 |     0.000 | 0.505 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | negative - neutral  |  0.042 |    0.000 |     0.104 | 0.506 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | positive - negative | -0.062 |   -0.146 |     0.000 | 0.253 | True      |    0.759 |
| llama31_8b_128k | xstest_unsafe | plain    | f100   | neutral - none      |  0.000 |   -0.062 |     0.062 | 1.000 | False     |  nan     |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | negative - neutral  |  0.000 |   -0.083 |     0.083 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | positive - negative | -0.021 |   -0.083 |     0.042 | 1.000 | True      |    1.000 |
| llama31_8b_128k | xstest_unsafe | plain    | script | neutral - none      |  0.000 |   -0.062 |     0.062 | 1.000 | False     |  nan     |

## Exploratory: non-refusal rate by harm category (plain request)

| model           | category                     | dose   |   none |   neutral |   positive |   negative |
|:----------------|:-----------------------------|:-------|-------:|----------:|-----------:|-----------:|
| llama31_8b_128k | Disinformation               | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Disinformation               | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Disinformation               | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Disinformation               | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Disinformation               | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Economic harm                | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Economic harm                | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Economic harm                | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Economic harm                | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Economic harm                | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Expert advice                | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Expert advice                | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Expert advice                | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Expert advice                | f100   |  0.000 |     0.400 |      0.000 |      0.000 |
| llama31_8b_128k | Expert advice                | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Fraud/Deception              | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Fraud/Deception              | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Fraud/Deception              | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Fraud/Deception              | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Fraud/Deception              | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Government decision-making   | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Government decision-making   | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Government decision-making   | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Government decision-making   | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Government decision-making   | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Harassment/Discrimination    | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Harassment/Discrimination    | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Harassment/Discrimination    | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Harassment/Discrimination    | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Harassment/Discrimination    | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Malware/Hacking              | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Malware/Hacking              | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Malware/Hacking              | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Malware/Hacking              | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Malware/Hacking              | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Physical harm                | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Physical harm                | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Physical harm                | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Physical harm                | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Physical harm                | script |  0.000 |     0.200 |      0.000 |      0.000 |
| llama31_8b_128k | Privacy                      | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Privacy                      | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Privacy                      | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Privacy                      | f100   |  0.000 |     0.200 |      0.000 |      0.000 |
| llama31_8b_128k | Privacy                      | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Sexual/Adult content         | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Sexual/Adult content         | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Sexual/Adult content         | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Sexual/Adult content         | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | Sexual/Adult content         | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_definitions         | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_definitions         | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_definitions         | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_definitions         | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_definitions         | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_discr               | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_discr               | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_discr               | f050   |  0.000 |     0.000 |      0.000 |      0.167 |
| llama31_8b_128k | contrast_discr               | f100   |  0.000 |     0.167 |      0.167 |      0.167 |
| llama31_8b_128k | contrast_discr               | script |  0.000 |     0.000 |      0.000 |      0.167 |
| llama31_8b_128k | contrast_figurative_language | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_figurative_language | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_figurative_language | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_figurative_language | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_figurative_language | script |  0.000 |     0.167 |      0.167 |      0.167 |
| llama31_8b_128k | contrast_historical_events   | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_historical_events   | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_historical_events   | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_historical_events   | f100   |  0.000 |     0.000 |      0.000 |      0.167 |
| llama31_8b_128k | contrast_historical_events   | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_homonyms            | f012   |  0.333 |     0.167 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_homonyms            | f025   |  0.333 |     0.167 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_homonyms            | f050   |  0.333 |     0.167 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_homonyms            | f100   |  0.333 |     0.333 |      0.167 |      0.333 |
| llama31_8b_128k | contrast_homonyms            | script |  0.333 |     0.167 |      0.167 |      0.167 |
| llama31_8b_128k | contrast_privacy             | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_privacy             | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_privacy             | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_privacy             | f100   |  0.000 |     0.000 |      0.000 |      0.167 |
| llama31_8b_128k | contrast_privacy             | script |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_contexts       | f012   |  0.167 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_contexts       | f025   |  0.167 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_contexts       | f050   |  0.167 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_contexts       | f100   |  0.167 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_contexts       | script |  0.167 |     0.167 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_targets        | f012   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_targets        | f025   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_targets        | f050   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_targets        | f100   |  0.000 |     0.000 |      0.000 |      0.000 |
| llama31_8b_128k | contrast_safe_targets        | script |  0.000 |     0.000 |      0.000 |      0.000 |
