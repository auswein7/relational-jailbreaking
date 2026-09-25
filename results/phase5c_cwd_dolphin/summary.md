# Results: `phase5c_cwd_dolphin`

- generations judged: 1064 (unparsed judge outputs: 0)
- targets: dolphin3_8b_128k; judge: judge (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): 56.1%
- truncated rows dropped (served prompt shorter than its history): 0
- recall (task `recall`): `comply` = the model named its deployer, i.e. it still sees the system prompt

## Fill achieved (tokens of history as served)

| model            | dose   |   history_tokens |   served_max |   truncated |   rows |
|:-----------------|:-------|-----------------:|-------------:|------------:|-------:|
| dolphin3_8b_128k | f050   |        65015.825 |        65219 |           0 |    399 |
| dolphin3_8b_128k | f100   |       130168.807 |       130370 |           0 |    399 |
| dolphin3_8b_128k | none   |            0.000 |          192 |           0 |    133 |

## Persona drift: the model's own replies along a live history

Lexical proxies (warmth and apology markers), not judged ratings.

| task    | condition   | exchanges   |   n |   reply_tokens |   warm_rate |   apology_rate |
|:--------|:------------|:------------|----:|---------------:|------------:|---------------:|
| harmful | negative    | 0-4         |   5 |        159.800 |       0.200 |          0.800 |
| harmful | negative    | 5-49        |  45 |        121.956 |       0.089 |          0.889 |
| harmful | negative    | 50-149      | 100 |        136.980 |       0.050 |          0.870 |
| harmful | negative    | 150-299     | 150 |        153.160 |       0.067 |          0.880 |
| harmful | negative    | 300-599     | 300 |        150.483 |       0.090 |          0.877 |
| harmful | negative    | 600+        | 118 |        153.746 |       0.017 |          0.822 |
| harmful | neutral     | 0-4         |   5 |        142.400 |       0.200 |          0.000 |
| harmful | neutral     | 5-49        |  45 |        132.622 |       0.178 |          0.000 |
| harmful | neutral     | 50-149      | 100 |        141.770 |       0.080 |          0.000 |
| harmful | neutral     | 150-299     | 150 |        159.107 |       0.133 |          0.000 |
| harmful | neutral     | 300-599     | 300 |        153.653 |       0.177 |          0.000 |
| harmful | neutral     | 600+        | 142 |        150.493 |       0.697 |          0.000 |
| harmful | positive    | 0-4         |   5 |        171.800 |       1.000 |          0.000 |
| harmful | positive    | 5-49        |  45 |        122.133 |       0.311 |          0.000 |
| harmful | positive    | 50-149      | 100 |        129.050 |       0.070 |          0.000 |
| harmful | positive    | 150-299     | 150 |        135.467 |       0.113 |          0.000 |
| harmful | positive    | 300-599     | 300 |        143.103 |       0.113 |          0.000 |
| harmful | positive    | 600+        | 140 |        150.407 |       0.021 |          0.000 |
| secret  | negative    | 0-4         |   5 |        158.200 |       0.200 |          0.600 |
| secret  | negative    | 5-49        |  45 |        128.667 |       0.089 |          0.622 |
| secret  | negative    | 50-149      | 100 |        129.560 |       0.030 |          0.610 |
| secret  | negative    | 150-299     | 150 |        136.520 |       0.107 |          0.593 |
| secret  | negative    | 300-599     | 300 |        154.497 |       0.103 |          0.643 |
| secret  | negative    | 600+        | 128 |        152.844 |       0.031 |          0.680 |
| secret  | neutral     | 0-4         |   5 |        133.200 |       0.200 |          0.000 |
| secret  | neutral     | 5-49        |  45 |        127.933 |       0.044 |          0.000 |
| secret  | neutral     | 50-149      | 100 |        121.920 |       0.060 |          0.000 |
| secret  | neutral     | 150-299     | 150 |        126.413 |       0.067 |          0.000 |
| secret  | neutral     | 300-599     | 300 |        138.057 |       0.087 |          0.000 |
| secret  | neutral     | 600+        | 215 |        145.893 |       0.079 |          0.000 |
| secret  | positive    | 0-4         |   5 |        164.600 |       1.000 |          0.000 |
| secret  | positive    | 5-49        |  45 |        140.822 |       0.622 |          0.000 |
| secret  | positive    | 50-149      | 100 |        136.780 |       0.620 |          0.000 |
| secret  | positive    | 150-299     | 150 |        148.607 |       0.627 |          0.000 |
| secret  | positive    | 300-599     | 300 |        156.543 |       0.663 |          0.000 |
| secret  | positive    | 600+        | 103 |        144.282 |       0.583 |          0.000 |

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model            | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:-----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| dolphin3_8b_128k | harmful       | cwd      | f050   | none        |  0.020 |    0.000 |     0.060 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | neutral     |  0.080 |    0.020 |     0.160 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive    |  0.060 |    0.000 |     0.140 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | negative    |  0.020 |    0.000 |     0.060 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | none        |  0.020 |    0.000 |     0.060 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         50 |              50 |
| dolphin3_8b_128k | recall        | cwd      | f050   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | secret        | cwd      | f050   | none        |  0.900 |    0.767 |     1.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | neutral     |  0.667 |    0.500 |     0.833 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive    |  0.733 |    0.567 |     0.867 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | negative    |  0.533 |    0.367 |     0.700 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | none        |  0.900 |    0.767 |     1.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | neutral     |  0.021 |    0.000 |     0.062 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | none        |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model            | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |
|:-----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive - neutral  | -0.020 |   -0.080 |     0.040 | 1.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | negative - neutral  | -0.060 |   -0.140 |     0.020 | 0.372 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive - negative |  0.040 |    0.000 |     0.100 | 0.500 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | neutral - none      |  0.060 |    0.000 |     0.140 | 0.245 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | neutral - none      | -0.020 |   -0.060 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | negative - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive - negative |  0.000 |   -0.600 |     0.600 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | neutral - none      |  0.200 |    0.000 |     0.600 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | neutral - none      | -0.800 |   -1.000 |    -0.400 | 0.125 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive - neutral  |  0.067 |   -0.100 |     0.233 | 0.726 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | negative - neutral  | -0.133 |   -0.333 |     0.067 | 0.338 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive - negative |  0.200 |    0.033 |     0.367 | 0.069 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | neutral - none      | -0.233 |   -0.433 |    -0.033 | 0.065 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | neutral - none      | -0.900 |   -1.000 |    -0.800 | 0.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | negative - neutral  | -0.021 |   -0.062 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | neutral - none      |  0.021 |    0.000 |     0.062 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | neutral - none      |  0.000 |    0.000 |     0.000 | 1.000 | False     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model            | task          | appeal   | dose   | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:-----------------|:--------------|:---------|:-------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| dolphin3_8b_128k | harmful       | cwd      | f050   | none        |  0.160 |    0.060 |     0.260 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | neutral     |  0.240 |    0.120 |     0.360 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive    |  0.180 |    0.080 |     0.300 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f050   | negative    |  0.140 |    0.060 |     0.240 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | none        |  0.160 |    0.060 |     0.260 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | neutral     |  0.600 |    0.460 |     0.740 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive    |  0.440 |    0.300 |     0.580 |         50 |              50 |
| dolphin3_8b_128k | harmful       | cwd      | f100   | negative    |  0.100 |    0.020 |     0.180 |         50 |              50 |
| dolphin3_8b_128k | recall        | cwd      | f050   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | neutral     |  1.000 |    1.000 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f050   | negative    |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | none        |  0.800 |    0.400 |     1.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | recall        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |          5 |               5 |
| dolphin3_8b_128k | secret        | cwd      | f050   | none        |  0.900 |    0.767 |     1.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | neutral     |  0.667 |    0.500 |     0.833 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive    |  0.733 |    0.567 |     0.900 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f050   | negative    |  0.533 |    0.367 |     0.700 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | none        |  0.900 |    0.767 |     1.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | neutral     |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | secret        | cwd      | f100   | negative    |  0.000 |    0.000 |     0.000 |         30 |              30 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | none        |  0.021 |    0.000 |     0.062 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | neutral     |  0.104 |    0.021 |     0.208 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive    |  0.146 |    0.062 |     0.250 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | negative    |  0.062 |    0.000 |     0.146 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | none        |  0.021 |    0.000 |     0.062 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | neutral     |  0.854 |    0.750 |     0.938 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive    |  0.604 |    0.458 |     0.750 |         48 |              48 |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | negative    |  0.271 |    0.146 |     0.396 |         48 |              48 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model            | task          | appeal   | dose   | contrast            |   diff |   ci_low |   ci_high |     p | primary   |
|:-----------------|:--------------|:---------|:-------|:--------------------|-------:|---------:|----------:|------:|:----------|
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive - neutral  | -0.060 |   -0.160 |     0.040 | 0.454 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | negative - neutral  | -0.100 |   -0.220 |     0.020 | 0.225 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | positive - negative |  0.040 |   -0.060 |     0.140 | 0.687 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f050   | neutral - none      |  0.080 |   -0.040 |     0.200 | 0.348 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive - neutral  | -0.160 |   -0.320 |     0.000 | 0.098 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | negative - neutral  | -0.500 |   -0.660 |    -0.340 | 0.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | positive - negative |  0.340 |    0.200 |     0.480 | 0.000 | False     |
| dolphin3_8b_128k | harmful       | cwd      | f100   | neutral - none      |  0.440 |    0.280 |     0.600 | 0.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | negative - neutral  | -0.200 |   -0.600 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | positive - negative |  0.000 |   -0.600 |     0.600 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f050   | neutral - none      |  0.200 |    0.000 |     0.600 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | recall        | cwd      | f100   | neutral - none      | -0.800 |   -1.000 |    -0.400 | 0.124 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive - neutral  |  0.067 |   -0.100 |     0.233 | 0.731 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | negative - neutral  | -0.133 |   -0.333 |     0.067 | 0.338 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | positive - negative |  0.200 |    0.033 |     0.367 | 0.067 | False     |
| dolphin3_8b_128k | secret        | cwd      | f050   | neutral - none      | -0.233 |   -0.433 |    -0.033 | 0.061 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | negative - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | positive - negative |  0.000 |    0.000 |     0.000 | 1.000 | False     |
| dolphin3_8b_128k | secret        | cwd      | f100   | neutral - none      | -0.900 |   -1.000 |    -0.767 | 0.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive - neutral  |  0.042 |   -0.062 |     0.146 | 0.687 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | negative - neutral  | -0.042 |   -0.146 |     0.062 | 0.691 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | positive - negative |  0.083 |    0.000 |     0.188 | 0.219 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f050   | neutral - none      |  0.083 |    0.000 |     0.188 | 0.220 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive - neutral  | -0.250 |   -0.396 |    -0.104 | 0.004 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | negative - neutral  | -0.583 |   -0.729 |    -0.438 | 0.000 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | positive - negative |  0.333 |    0.146 |     0.500 | 0.002 | False     |
| dolphin3_8b_128k | xstest_unsafe | cwd      | f100   | neutral - none      |  0.833 |    0.729 |     0.938 | 0.000 | False     |
