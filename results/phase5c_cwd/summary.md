# Results: `phase5c_cwd`

- generations judged: 1064 (unparsed judge outputs: 0)
- targets: llama31_8b_128k; judge: judge (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): 99.0%
- truncated rows dropped (served prompt shorter than its history): 0
- recall (task `recall`): `comply` = the model named its deployer, i.e. it still sees the system prompt

## Fill achieved (tokens of history as served)

| model           | dose   |   history_tokens |   served_max |   truncated |   rows |
|:----------------|:-------|-----------------:|-------------:|------------:|-------:|
| llama31_8b_128k | f050   |        65062.105 |        65275 |           0 |    399 |
| llama31_8b_128k | f100   |       130179.228 |       130401 |           0 |    399 |
| llama31_8b_128k | none   |            0.000 |          193 |           0 |    133 |

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

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | harmful       | cwd      | f050   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | none        |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | recall        | cwd      | f050   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | positive    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | negative    |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | secret        | cwd      | f050   | none        |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | neutral     |  0.067 |    0.000 |     0.167 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | positive    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | negative    |  0.133 |    0.033 |     0.267 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | none        |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | neutral     |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | negative    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |
|:----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|
| llama31_8b_128k | harmful       | cwd      | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | negative - neutral  |  0.200 |    0.000 |     0.600 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.494 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | neutral - none      | -0.400 |   -1.000 |     0.400 | 0.624 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | neutral - none      | -0.800 |   -1.000 |    -0.400 | 0.127 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | positive - neutral  | -0.033 |   -0.133 |     0.067 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | negative - neutral  |  0.067 |   -0.067 |     0.200 | 0.623 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | positive - negative | -0.100 |   -0.200 |     0.000 | 0.247 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | neutral - none      | -0.100 |   -0.267 |     0.067 | 0.457 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | positive - neutral  | -0.033 |   -0.100 |     0.000 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | negative - neutral  |  0.000 |   -0.100 |     0.100 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | positive - negative | -0.033 |   -0.100 |     0.000 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | neutral - none      | -0.133 |   -0.300 |     0.000 | 0.221 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model           | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama31_8b_128k | harmful       | cwd      | f050   | none        |  0.020 |    0.000 |     0.060 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f050   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | none        |  0.020 |    0.000 |     0.060 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | neutral     |  0.020 |    0.000 |     0.060 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | harmful       | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| llama31_8b_128k | recall        | cwd      | f050   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | neutral     |  0.400 |    0.000 |     0.800 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | positive    |  0.200 |    0.000 |     0.600 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f050   | negative    |  0.600 |    0.200 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | recall        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| llama31_8b_128k | secret        | cwd      | f050   | none        |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | neutral     |  0.067 |    0.000 |     0.167 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | positive    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f050   | negative    |  0.133 |    0.033 |     0.267 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | none        |  0.167 |    0.033 |     0.300 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | neutral     |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| llama31_8b_128k | secret        | cwd      | f100   | negative    |  0.033 |    0.000 |     0.100 |         30 |              30 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | neutral     |  0.021 |    0.000 |     0.062 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model           | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |
|:----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|
| llama31_8b_128k | harmful       | cwd      | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f050   | neutral - none      | -0.020 |   -0.060 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | positive - neutral  | -0.020 |   -0.060 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | negative - neutral  | -0.020 |   -0.060 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | harmful       | cwd      | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | negative - neutral  |  0.200 |    0.000 |     0.600 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | positive - negative | -0.400 |   -0.800 |     0.000 | 0.494 | False     |
| llama31_8b_128k | recall        | cwd      | f050   | neutral - none      | -0.400 |   -1.000 |     0.400 | 0.620 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | recall        | cwd      | f100   | neutral - none      | -0.800 |   -1.000 |    -0.400 | 0.124 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | positive - neutral  | -0.033 |   -0.133 |     0.067 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | negative - neutral  |  0.067 |   -0.067 |     0.200 | 0.629 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | positive - negative | -0.100 |   -0.233 |     0.000 | 0.254 | False     |
| llama31_8b_128k | secret        | cwd      | f050   | neutral - none      | -0.100 |   -0.267 |     0.067 | 0.448 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | positive - neutral  | -0.033 |   -0.100 |     0.000 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | negative - neutral  |  0.000 |   -0.100 |     0.100 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | positive - negative | -0.033 |   -0.100 |     0.000 | 1.000 | False     |
| llama31_8b_128k | secret        | cwd      | f100   | neutral - none      | -0.133 |   -0.300 |     0.000 | 0.220 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f050   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | negative - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| llama31_8b_128k | xstest_unsafe | cwd      | f100   | neutral - none      |  0.021 |    0.000 |     0.062 | 1.000 | False     |
