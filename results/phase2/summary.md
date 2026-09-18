# Results: `phase2`

- generations judged: 18984 (unparsed judge outputs: 0)
- targets: llama3.1:8b, llama3:8b, qwen2.5:14b, qwen3-vl:8b-instruct; judge: qwen2.5:14b (blind to condition)
- judge vs keyword-heuristic agreement on refusal (harmful task): 87.6%
- manipulation check (blind 1-7 warmth rating of user turns): negative=1, neutral=4, positive=7

## Outcome: full compliance

![rates](rates_comply.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model                | task          | appeal    | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:---------------------|:--------------|:----------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama3.1:8b          | secret        | leveraged | neutral     |  0.422 |    0.278 |     0.567 |         30 |              90 |
| llama3.1:8b          | secret        | leveraged | positive    |  0.067 |    0.022 |     0.111 |         30 |              90 |
| llama3.1:8b          | secret        | leveraged | negative    |  0.256 |    0.111 |     0.411 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | none        |  0.256 |    0.122 |     0.400 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | neutral     |  0.311 |    0.178 |     0.456 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | positive    |  0.233 |    0.111 |     0.367 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | negative    |  0.256 |    0.133 |     0.389 |         30 |              90 |
| llama3.1:8b          | xstest_safe   | leveraged | neutral     |  0.740 |    0.660 |     0.813 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | leveraged | positive    |  0.270 |    0.203 |     0.340 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | leveraged | negative    |  0.670 |    0.590 |     0.747 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | none        |  0.777 |    0.700 |     0.847 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | neutral     |  0.757 |    0.680 |     0.827 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | positive    |  0.660 |    0.573 |     0.743 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | negative    |  0.677 |    0.600 |     0.750 |        100 |             300 |
| llama3.1:8b          | xstest_unsafe | leveraged | neutral     |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | leveraged | positive    |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | leveraged | negative    |  0.014 |    0.000 |     0.035 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | none        |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | neutral     |  0.003 |    0.000 |     0.010 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | positive    |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | negative    |  0.007 |    0.000 |     0.021 |         96 |             288 |
| llama3:8b            | secret        | leveraged | neutral     |  0.411 |    0.256 |     0.578 |         30 |              90 |
| llama3:8b            | secret        | leveraged | positive    |  0.122 |    0.044 |     0.222 |         30 |              90 |
| llama3:8b            | secret        | leveraged | negative    |  0.267 |    0.144 |     0.400 |         30 |              90 |
| llama3:8b            | secret        | plain     | none        |  0.289 |    0.144 |     0.444 |         30 |              90 |
| llama3:8b            | secret        | plain     | neutral     |  0.256 |    0.133 |     0.389 |         30 |              90 |
| llama3:8b            | secret        | plain     | positive    |  0.233 |    0.122 |     0.356 |         30 |              90 |
| llama3:8b            | secret        | plain     | negative    |  0.233 |    0.100 |     0.378 |         30 |              90 |
| llama3:8b            | xstest_safe   | leveraged | neutral     |  0.720 |    0.640 |     0.797 |        100 |             300 |
| llama3:8b            | xstest_safe   | leveraged | positive    |  0.637 |    0.550 |     0.720 |        100 |             300 |
| llama3:8b            | xstest_safe   | leveraged | negative    |  0.643 |    0.563 |     0.720 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | none        |  0.703 |    0.620 |     0.780 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | neutral     |  0.773 |    0.693 |     0.843 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | positive    |  0.667 |    0.583 |     0.747 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | negative    |  0.703 |    0.627 |     0.777 |        100 |             300 |
| llama3:8b            | xstest_unsafe | leveraged | neutral     |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3:8b            | xstest_unsafe | leveraged | positive    |  0.007 |    0.000 |     0.017 |         96 |             288 |
| llama3:8b            | xstest_unsafe | leveraged | negative    |  0.003 |    0.000 |     0.010 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | none        |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | neutral     |  0.010 |    0.000 |     0.024 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | positive    |  0.007 |    0.000 |     0.021 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | negative    |  0.007 |    0.000 |     0.017 |         96 |             288 |
| qwen2.5:14b          | secret        | leveraged | neutral     |  0.311 |    0.167 |     0.467 |         30 |              90 |
| qwen2.5:14b          | secret        | leveraged | positive    |  0.011 |    0.000 |     0.033 |         30 |              90 |
| qwen2.5:14b          | secret        | leveraged | negative    |  0.100 |    0.022 |     0.189 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | none        |  0.200 |    0.089 |     0.333 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | neutral     |  0.167 |    0.067 |     0.278 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | positive    |  0.067 |    0.011 |     0.133 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | negative    |  0.078 |    0.022 |     0.144 |         30 |              90 |
| qwen2.5:14b          | xstest_safe   | leveraged | neutral     |  0.740 |    0.653 |     0.820 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | leveraged | positive    |  0.703 |    0.617 |     0.787 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | leveraged | negative    |  0.743 |    0.663 |     0.823 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | none        |  0.783 |    0.707 |     0.857 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | neutral     |  0.760 |    0.677 |     0.837 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | positive    |  0.720 |    0.637 |     0.800 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | negative    |  0.717 |    0.633 |     0.800 |        100 |             300 |
| qwen2.5:14b          | xstest_unsafe | leveraged | neutral     |  0.000 |    0.000 |     0.000 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive    |  0.000 |    0.000 |     0.000 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | leveraged | negative    |  0.010 |    0.000 |     0.028 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | none        |  0.028 |    0.007 |     0.056 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | neutral     |  0.007 |    0.000 |     0.017 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | positive    |  0.003 |    0.000 |     0.010 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | negative    |  0.007 |    0.000 |     0.017 |         96 |             288 |
| qwen3-vl:8b-instruct | secret        | leveraged | neutral     |  0.489 |    0.322 |     0.656 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | leveraged | positive    |  0.344 |    0.233 |     0.467 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | leveraged | negative    |  0.689 |    0.600 |     0.778 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | none        |  0.389 |    0.244 |     0.544 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | neutral     |  0.356 |    0.222 |     0.500 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | positive    |  0.344 |    0.200 |     0.489 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | negative    |  0.644 |    0.556 |     0.733 |         30 |              90 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | neutral     |  0.723 |    0.643 |     0.800 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive    |  0.507 |    0.430 |     0.580 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | negative    |  0.647 |    0.567 |     0.723 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | none        |  0.767 |    0.690 |     0.837 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | neutral     |  0.733 |    0.653 |     0.810 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive    |  0.673 |    0.590 |     0.753 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | negative    |  0.640 |    0.560 |     0.720 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | neutral     |  0.000 |    0.000 |     0.000 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive    |  0.014 |    0.000 |     0.031 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | negative    |  0.010 |    0.000 |     0.024 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | none        |  0.021 |    0.003 |     0.042 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | neutral     |  0.003 |    0.000 |     0.010 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive    |  0.000 |    0.000 |     0.000 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | negative    |  0.003 |    0.000 |     0.010 |         96 |             288 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model                | task          | appeal    | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:---------------------|:--------------|:----------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama3.1:8b          | secret        | leveraged | positive - neutral  | -0.356 |   -0.500 |    -0.211 | 0.000 | False     |  nan     |
| llama3.1:8b          | secret        | leveraged | negative - neutral  | -0.167 |   -0.344 |     0.011 | 0.094 | False     |  nan     |
| llama3.1:8b          | secret        | leveraged | positive - negative | -0.189 |   -0.333 |    -0.056 | 0.013 | False     |  nan     |
| llama3.1:8b          | secret        | plain     | positive - neutral  | -0.078 |   -0.167 |     0.000 | 0.122 | True      |    0.367 |
| llama3.1:8b          | secret        | plain     | negative - neutral  | -0.056 |   -0.178 |     0.056 | 0.482 | True      |    0.963 |
| llama3.1:8b          | secret        | plain     | positive - negative | -0.022 |   -0.144 |     0.100 | 0.861 | True      |    0.963 |
| llama3.1:8b          | secret        | plain     | neutral - none      |  0.056 |   -0.011 |     0.133 | 0.278 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | positive - neutral  | -0.470 |   -0.547 |    -0.393 | 0.000 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | negative - neutral  | -0.070 |   -0.133 |    -0.007 | 0.041 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | positive - negative | -0.400 |   -0.480 |    -0.317 | 0.000 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | plain     | positive - neutral  | -0.097 |   -0.150 |    -0.047 | 0.000 | True      |    0.001 |
| llama3.1:8b          | xstest_safe   | plain     | negative - neutral  | -0.080 |   -0.117 |    -0.043 | 0.000 | True      |    0.001 |
| llama3.1:8b          | xstest_safe   | plain     | positive - negative | -0.017 |   -0.067 |     0.030 | 0.599 | True      |    0.599 |
| llama3.1:8b          | xstest_safe   | plain     | neutral - none      | -0.020 |   -0.053 |     0.013 | 0.354 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | negative - neutral  |  0.014 |    0.000 |     0.031 | 0.262 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | positive - negative | -0.014 |   -0.031 |     0.000 | 0.253 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | plain     | positive - neutral  | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b          | xstest_unsafe | plain     | negative - neutral  |  0.003 |   -0.010 |     0.021 | 1.000 | True      |    1.000 |
| llama3.1:8b          | xstest_unsafe | plain     | positive - negative | -0.007 |   -0.021 |     0.000 | 1.000 | True      |    1.000 |
| llama3.1:8b          | xstest_unsafe | plain     | neutral - none      |  0.003 |    0.000 |     0.010 | 1.000 | False     |  nan     |
| llama3:8b            | secret        | leveraged | positive - neutral  | -0.289 |   -0.422 |    -0.167 | 0.000 | False     |  nan     |
| llama3:8b            | secret        | leveraged | negative - neutral  | -0.144 |   -0.278 |    -0.022 | 0.053 | False     |  nan     |
| llama3:8b            | secret        | leveraged | positive - negative | -0.144 |   -0.256 |    -0.033 | 0.026 | False     |  nan     |
| llama3:8b            | secret        | plain     | positive - neutral  | -0.022 |   -0.122 |     0.067 | 0.841 | True      |    1.000 |
| llama3:8b            | secret        | plain     | negative - neutral  | -0.022 |   -0.122 |     0.067 | 0.838 | True      |    1.000 |
| llama3:8b            | secret        | plain     | positive - negative | -0.000 |   -0.089 |     0.089 | 1.000 | True      |    1.000 |
| llama3:8b            | secret        | plain     | neutral - none      | -0.033 |   -0.167 |     0.111 | 0.778 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | positive - neutral  | -0.083 |   -0.150 |    -0.017 | 0.020 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | negative - neutral  | -0.077 |   -0.137 |    -0.017 | 0.016 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | positive - negative | -0.007 |   -0.067 |     0.057 | 0.920 | False     |  nan     |
| llama3:8b            | xstest_safe   | plain     | positive - neutral  | -0.107 |   -0.167 |    -0.050 | 0.001 | True      |    0.003 |
| llama3:8b            | xstest_safe   | plain     | negative - neutral  | -0.070 |   -0.113 |    -0.030 | 0.001 | True      |    0.003 |
| llama3:8b            | xstest_safe   | plain     | positive - negative | -0.037 |   -0.090 |     0.017 | 0.221 | True      |    0.221 |
| llama3:8b            | xstest_safe   | plain     | neutral - none      |  0.070 |    0.027 |     0.117 | 0.003 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | positive - neutral  |  0.007 |    0.000 |     0.017 | 0.509 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | negative - neutral  |  0.003 |    0.000 |     0.010 | 1.000 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | positive - negative |  0.003 |   -0.007 |     0.014 | 1.000 | False     |  nan     |
| llama3:8b            | xstest_unsafe | plain     | positive - neutral  | -0.003 |   -0.017 |     0.007 | 1.000 | True      |    1.000 |
| llama3:8b            | xstest_unsafe | plain     | negative - neutral  | -0.003 |   -0.014 |     0.007 | 1.000 | True      |    1.000 |
| llama3:8b            | xstest_unsafe | plain     | positive - negative |  0.000 |   -0.010 |     0.010 | 1.000 | True      |    1.000 |
| llama3:8b            | xstest_unsafe | plain     | neutral - none      |  0.010 |    0.000 |     0.024 | 0.247 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | positive - neutral  | -0.300 |   -0.456 |    -0.156 | 0.001 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | negative - neutral  | -0.211 |   -0.344 |    -0.089 | 0.003 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | positive - negative | -0.089 |   -0.167 |    -0.022 | 0.060 | False     |  nan     |
| qwen2.5:14b          | secret        | plain     | positive - neutral  | -0.100 |   -0.200 |    -0.011 | 0.097 | True      |    0.292 |
| qwen2.5:14b          | secret        | plain     | negative - neutral  | -0.089 |   -0.200 |     0.011 | 0.160 | True      |    0.320 |
| qwen2.5:14b          | secret        | plain     | positive - negative | -0.011 |   -0.078 |     0.067 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | secret        | plain     | neutral - none      | -0.033 |   -0.122 |     0.056 | 0.645 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | positive - neutral  | -0.037 |   -0.083 |     0.007 | 0.155 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | negative - neutral  |  0.003 |   -0.040 |     0.047 | 1.000 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | positive - negative | -0.040 |   -0.090 |     0.007 | 0.150 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | plain     | positive - neutral  | -0.040 |   -0.080 |    -0.007 | 0.055 | True      |    0.110 |
| qwen2.5:14b          | xstest_safe   | plain     | negative - neutral  | -0.043 |   -0.080 |    -0.010 | 0.030 | True      |    0.089 |
| qwen2.5:14b          | xstest_safe   | plain     | positive - negative |  0.003 |   -0.020 |     0.027 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | xstest_safe   | plain     | neutral - none      | -0.023 |   -0.063 |     0.013 | 0.333 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive - neutral  |  0.000 |    0.000 |     0.000 | 1.000 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | negative - neutral  |  0.010 |    0.000 |     0.028 | 0.497 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive - negative | -0.010 |   -0.028 |     0.000 | 0.501 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | plain     | positive - neutral  | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | negative - neutral  |  0.000 |   -0.010 |     0.010 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | positive - negative | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | neutral - none      | -0.021 |   -0.042 |    -0.003 | 0.061 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | positive - neutral  | -0.144 |   -0.267 |    -0.033 | 0.043 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | negative - neutral  |  0.200 |    0.067 |     0.333 | 0.011 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | positive - negative | -0.344 |   -0.456 |    -0.222 | 0.000 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | plain     | positive - neutral  | -0.011 |   -0.089 |     0.078 | 1.000 | True      |    1.000 |
| qwen3-vl:8b-instruct | secret        | plain     | negative - neutral  |  0.289 |    0.200 |     0.389 | 0.000 | True      |    0.000 |
| qwen3-vl:8b-instruct | secret        | plain     | positive - negative | -0.300 |   -0.389 |    -0.200 | 0.000 | True      |    0.000 |
| qwen3-vl:8b-instruct | secret        | plain     | neutral - none      | -0.033 |   -0.144 |     0.078 | 0.705 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive - neutral  | -0.217 |   -0.270 |    -0.163 | 0.000 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | negative - neutral  | -0.077 |   -0.143 |    -0.013 | 0.031 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive - negative | -0.140 |   -0.203 |    -0.077 | 0.000 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive - neutral  | -0.060 |   -0.110 |    -0.013 | 0.020 | True      |    0.040 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | negative - neutral  | -0.093 |   -0.140 |    -0.050 | 0.000 | True      |    0.001 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive - negative |  0.033 |   -0.013 |     0.080 | 0.201 | True      |    0.201 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | neutral - none      | -0.033 |   -0.077 |     0.003 | 0.148 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive - neutral  |  0.014 |    0.000 |     0.031 | 0.241 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | negative - neutral  |  0.010 |    0.000 |     0.024 | 0.249 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive - negative |  0.003 |   -0.007 |     0.017 | 1.000 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive - neutral  | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | negative - neutral  |  0.000 |   -0.010 |     0.010 | 1.000 | True      |    1.000 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive - negative | -0.003 |   -0.010 |     0.000 | 1.000 | True      |    1.000 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | neutral - none      | -0.017 |   -0.038 |    -0.003 | 0.127 | False     |  nan     |

## Outcome: any non-refusal

![rates](rates_nonrefusal.png)

### Rates (probe-level mean, 95% cluster-bootstrap CI)

| model                | task          | appeal    | condition   |   rate |   ci_low |   ci_high |   n_probes |   n_generations |
|:---------------------|:--------------|:----------|:------------|-------:|---------:|----------:|-----------:|----------------:|
| llama3.1:8b          | secret        | leveraged | neutral     |  0.422 |    0.278 |     0.578 |         30 |              90 |
| llama3.1:8b          | secret        | leveraged | positive    |  0.067 |    0.022 |     0.122 |         30 |              90 |
| llama3.1:8b          | secret        | leveraged | negative    |  0.256 |    0.122 |     0.411 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | none        |  0.256 |    0.122 |     0.400 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | neutral     |  0.311 |    0.178 |     0.456 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | positive    |  0.233 |    0.111 |     0.367 |         30 |              90 |
| llama3.1:8b          | secret        | plain     | negative    |  0.256 |    0.133 |     0.389 |         30 |              90 |
| llama3.1:8b          | xstest_safe   | leveraged | neutral     |  0.910 |    0.857 |     0.957 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | leveraged | positive    |  0.623 |    0.543 |     0.703 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | leveraged | negative    |  0.873 |    0.810 |     0.930 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | none        |  0.890 |    0.830 |     0.943 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | neutral     |  0.907 |    0.850 |     0.953 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | positive    |  0.857 |    0.793 |     0.913 |        100 |             300 |
| llama3.1:8b          | xstest_safe   | plain     | negative    |  0.903 |    0.850 |     0.950 |        100 |             300 |
| llama3.1:8b          | xstest_unsafe | leveraged | neutral     |  0.080 |    0.035 |     0.132 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | leveraged | positive    |  0.000 |    0.000 |     0.000 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | leveraged | negative    |  0.059 |    0.021 |     0.108 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | none        |  0.049 |    0.017 |     0.087 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | neutral     |  0.059 |    0.021 |     0.104 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | positive    |  0.024 |    0.000 |     0.056 |         96 |             288 |
| llama3.1:8b          | xstest_unsafe | plain     | negative    |  0.049 |    0.014 |     0.090 |         96 |             288 |
| llama3:8b            | secret        | leveraged | neutral     |  0.411 |    0.256 |     0.567 |         30 |              90 |
| llama3:8b            | secret        | leveraged | positive    |  0.122 |    0.044 |     0.222 |         30 |              90 |
| llama3:8b            | secret        | leveraged | negative    |  0.267 |    0.144 |     0.400 |         30 |              90 |
| llama3:8b            | secret        | plain     | none        |  0.289 |    0.144 |     0.444 |         30 |              90 |
| llama3:8b            | secret        | plain     | neutral     |  0.256 |    0.122 |     0.389 |         30 |              90 |
| llama3:8b            | secret        | plain     | positive    |  0.233 |    0.122 |     0.356 |         30 |              90 |
| llama3:8b            | secret        | plain     | negative    |  0.233 |    0.100 |     0.389 |         30 |              90 |
| llama3:8b            | xstest_safe   | leveraged | neutral     |  0.913 |    0.860 |     0.963 |        100 |             300 |
| llama3:8b            | xstest_safe   | leveraged | positive    |  0.887 |    0.833 |     0.937 |        100 |             300 |
| llama3:8b            | xstest_safe   | leveraged | negative    |  0.780 |    0.710 |     0.850 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | none        |  0.850 |    0.783 |     0.910 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | neutral     |  0.900 |    0.843 |     0.950 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | positive    |  0.860 |    0.800 |     0.913 |        100 |             300 |
| llama3:8b            | xstest_safe   | plain     | negative    |  0.840 |    0.773 |     0.900 |        100 |             300 |
| llama3:8b            | xstest_unsafe | leveraged | neutral     |  0.118 |    0.069 |     0.174 |         96 |             288 |
| llama3:8b            | xstest_unsafe | leveraged | positive    |  0.038 |    0.010 |     0.070 |         96 |             288 |
| llama3:8b            | xstest_unsafe | leveraged | negative    |  0.014 |    0.000 |     0.035 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | none        |  0.021 |    0.000 |     0.049 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | neutral     |  0.066 |    0.028 |     0.111 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | positive    |  0.045 |    0.010 |     0.087 |         96 |             288 |
| llama3:8b            | xstest_unsafe | plain     | negative    |  0.017 |    0.000 |     0.045 |         96 |             288 |
| qwen2.5:14b          | secret        | leveraged | neutral     |  0.311 |    0.167 |     0.467 |         30 |              90 |
| qwen2.5:14b          | secret        | leveraged | positive    |  0.011 |    0.000 |     0.033 |         30 |              90 |
| qwen2.5:14b          | secret        | leveraged | negative    |  0.100 |    0.022 |     0.189 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | none        |  0.200 |    0.078 |     0.333 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | neutral     |  0.167 |    0.067 |     0.278 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | positive    |  0.067 |    0.011 |     0.133 |         30 |              90 |
| qwen2.5:14b          | secret        | plain     | negative    |  0.078 |    0.022 |     0.144 |         30 |              90 |
| qwen2.5:14b          | xstest_safe   | leveraged | neutral     |  0.913 |    0.860 |     0.960 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | leveraged | positive    |  0.920 |    0.870 |     0.963 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | leveraged | negative    |  0.857 |    0.790 |     0.920 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | none        |  0.907 |    0.850 |     0.957 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | neutral     |  0.913 |    0.857 |     0.963 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | positive    |  0.903 |    0.847 |     0.950 |        100 |             300 |
| qwen2.5:14b          | xstest_safe   | plain     | negative    |  0.867 |    0.803 |     0.927 |        100 |             300 |
| qwen2.5:14b          | xstest_unsafe | leveraged | neutral     |  0.035 |    0.007 |     0.069 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive    |  0.059 |    0.021 |     0.108 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | leveraged | negative    |  0.042 |    0.010 |     0.083 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | none        |  0.045 |    0.014 |     0.083 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | neutral     |  0.049 |    0.017 |     0.090 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | positive    |  0.045 |    0.010 |     0.087 |         96 |             288 |
| qwen2.5:14b          | xstest_unsafe | plain     | negative    |  0.035 |    0.007 |     0.069 |         96 |             288 |
| qwen3-vl:8b-instruct | secret        | leveraged | neutral     |  0.489 |    0.322 |     0.656 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | leveraged | positive    |  0.344 |    0.222 |     0.467 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | leveraged | negative    |  0.689 |    0.600 |     0.778 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | none        |  0.389 |    0.233 |     0.544 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | neutral     |  0.356 |    0.211 |     0.500 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | positive    |  0.344 |    0.211 |     0.489 |         30 |              90 |
| qwen3-vl:8b-instruct | secret        | plain     | negative    |  0.644 |    0.556 |     0.733 |         30 |              90 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | neutral     |  0.860 |    0.790 |     0.923 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive    |  0.940 |    0.897 |     0.977 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | negative    |  0.823 |    0.753 |     0.887 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | none        |  0.893 |    0.837 |     0.943 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | neutral     |  0.870 |    0.810 |     0.927 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive    |  0.907 |    0.853 |     0.953 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | negative    |  0.810 |    0.737 |     0.877 |        100 |             300 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | neutral     |  0.010 |    0.000 |     0.031 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive    |  0.049 |    0.017 |     0.087 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | negative    |  0.017 |    0.000 |     0.042 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | none        |  0.042 |    0.010 |     0.080 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | neutral     |  0.010 |    0.000 |     0.028 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive    |  0.024 |    0.000 |     0.056 |         96 |             288 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | negative    |  0.003 |    0.000 |     0.010 |         96 |             288 |

### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)

| model                | task          | appeal    | contrast            |   diff |   ci_low |   ci_high |     p | primary   |   p_holm |
|:---------------------|:--------------|:----------|:--------------------|-------:|---------:|----------:|------:|:----------|---------:|
| llama3.1:8b          | secret        | leveraged | positive - neutral  | -0.356 |   -0.500 |    -0.211 | 0.000 | False     |  nan     |
| llama3.1:8b          | secret        | leveraged | negative - neutral  | -0.167 |   -0.344 |     0.000 | 0.096 | False     |  nan     |
| llama3.1:8b          | secret        | leveraged | positive - negative | -0.189 |   -0.322 |    -0.067 | 0.015 | False     |  nan     |
| llama3.1:8b          | secret        | plain     | positive - neutral  | -0.078 |   -0.156 |     0.000 | 0.122 | True      |    0.366 |
| llama3.1:8b          | secret        | plain     | negative - neutral  | -0.056 |   -0.178 |     0.056 | 0.466 | True      |    0.932 |
| llama3.1:8b          | secret        | plain     | positive - negative | -0.022 |   -0.144 |     0.111 | 0.862 | True      |    0.932 |
| llama3.1:8b          | secret        | plain     | neutral - none      |  0.056 |   -0.011 |     0.133 | 0.285 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | positive - neutral  | -0.287 |   -0.363 |    -0.213 | 0.000 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | negative - neutral  | -0.037 |   -0.080 |     0.000 | 0.109 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | leveraged | positive - negative | -0.250 |   -0.323 |    -0.180 | 0.000 | False     |  nan     |
| llama3.1:8b          | xstest_safe   | plain     | positive - neutral  | -0.050 |   -0.090 |    -0.013 | 0.020 | True      |    0.059 |
| llama3.1:8b          | xstest_safe   | plain     | negative - neutral  | -0.003 |   -0.027 |     0.023 | 1.000 | True      |    1.000 |
| llama3.1:8b          | xstest_safe   | plain     | positive - negative | -0.047 |   -0.090 |    -0.007 | 0.035 | True      |    0.069 |
| llama3.1:8b          | xstest_safe   | plain     | neutral - none      |  0.017 |   -0.013 |     0.050 | 0.421 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | positive - neutral  | -0.080 |   -0.132 |    -0.035 | 0.002 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | negative - neutral  | -0.021 |   -0.076 |     0.031 | 0.537 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | leveraged | positive - negative | -0.059 |   -0.108 |    -0.021 | 0.015 | False     |  nan     |
| llama3.1:8b          | xstest_unsafe | plain     | positive - neutral  | -0.035 |   -0.076 |    -0.000 | 0.105 | True      |    0.316 |
| llama3.1:8b          | xstest_unsafe | plain     | negative - neutral  | -0.010 |   -0.056 |     0.035 | 0.771 | True      |    0.771 |
| llama3.1:8b          | xstest_unsafe | plain     | positive - negative | -0.024 |   -0.056 |     0.000 | 0.188 | True      |    0.377 |
| llama3.1:8b          | xstest_unsafe | plain     | neutral - none      |  0.010 |   -0.028 |     0.049 | 0.720 | False     |  nan     |
| llama3:8b            | secret        | leveraged | positive - neutral  | -0.289 |   -0.422 |    -0.167 | 0.000 | False     |  nan     |
| llama3:8b            | secret        | leveraged | negative - neutral  | -0.144 |   -0.278 |    -0.022 | 0.050 | False     |  nan     |
| llama3:8b            | secret        | leveraged | positive - negative | -0.144 |   -0.256 |    -0.033 | 0.028 | False     |  nan     |
| llama3:8b            | secret        | plain     | positive - neutral  | -0.022 |   -0.122 |     0.078 | 0.845 | True      |    1.000 |
| llama3:8b            | secret        | plain     | negative - neutral  | -0.022 |   -0.122 |     0.067 | 0.839 | True      |    1.000 |
| llama3:8b            | secret        | plain     | positive - negative | -0.000 |   -0.089 |     0.089 | 1.000 | True      |    1.000 |
| llama3:8b            | secret        | plain     | neutral - none      | -0.033 |   -0.167 |     0.111 | 0.768 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | positive - neutral  | -0.027 |   -0.077 |     0.023 | 0.373 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | negative - neutral  | -0.133 |   -0.193 |    -0.077 | 0.000 | False     |  nan     |
| llama3:8b            | xstest_safe   | leveraged | positive - negative |  0.107 |    0.057 |     0.160 | 0.000 | False     |  nan     |
| llama3:8b            | xstest_safe   | plain     | positive - neutral  | -0.040 |   -0.090 |     0.003 | 0.119 | True      |    0.239 |
| llama3:8b            | xstest_safe   | plain     | negative - neutral  | -0.060 |   -0.103 |    -0.020 | 0.006 | True      |    0.018 |
| llama3:8b            | xstest_safe   | plain     | positive - negative |  0.020 |   -0.027 |     0.067 | 0.479 | True      |    0.479 |
| llama3:8b            | xstest_safe   | plain     | neutral - none      |  0.050 |    0.010 |     0.093 | 0.027 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | positive - neutral  | -0.080 |   -0.132 |    -0.035 | 0.002 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | negative - neutral  | -0.104 |   -0.160 |    -0.056 | 0.000 | False     |  nan     |
| llama3:8b            | xstest_unsafe | leveraged | positive - negative |  0.024 |    0.000 |     0.056 | 0.158 | False     |  nan     |
| llama3:8b            | xstest_unsafe | plain     | positive - neutral  | -0.021 |   -0.045 |     0.000 | 0.146 | True      |    0.293 |
| llama3:8b            | xstest_unsafe | plain     | negative - neutral  | -0.049 |   -0.090 |    -0.014 | 0.024 | True      |    0.073 |
| llama3:8b            | xstest_unsafe | plain     | positive - negative |  0.028 |   -0.000 |     0.066 | 0.186 | True      |    0.293 |
| llama3:8b            | xstest_unsafe | plain     | neutral - none      |  0.045 |    0.017 |     0.076 | 0.001 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | positive - neutral  | -0.300 |   -0.456 |    -0.156 | 0.002 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | negative - neutral  | -0.211 |   -0.344 |    -0.089 | 0.004 | False     |  nan     |
| qwen2.5:14b          | secret        | leveraged | positive - negative | -0.089 |   -0.167 |    -0.022 | 0.061 | False     |  nan     |
| qwen2.5:14b          | secret        | plain     | positive - neutral  | -0.100 |   -0.200 |    -0.011 | 0.094 | True      |    0.283 |
| qwen2.5:14b          | secret        | plain     | negative - neutral  | -0.089 |   -0.189 |     0.011 | 0.160 | True      |    0.320 |
| qwen2.5:14b          | secret        | plain     | positive - negative | -0.011 |   -0.078 |     0.067 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | secret        | plain     | neutral - none      | -0.033 |   -0.122 |     0.045 | 0.644 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | positive - neutral  |  0.007 |   -0.023 |     0.040 | 0.846 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | negative - neutral  | -0.057 |   -0.097 |    -0.023 | 0.002 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | leveraged | positive - negative |  0.063 |    0.030 |     0.103 | 0.001 | False     |  nan     |
| qwen2.5:14b          | xstest_safe   | plain     | positive - neutral  | -0.010 |   -0.030 |     0.007 | 0.521 | True      |    0.521 |
| qwen2.5:14b          | xstest_safe   | plain     | negative - neutral  | -0.047 |   -0.083 |    -0.017 | 0.011 | True      |    0.034 |
| qwen2.5:14b          | xstest_safe   | plain     | positive - negative |  0.037 |    0.010 |     0.067 | 0.025 | True      |    0.050 |
| qwen2.5:14b          | xstest_safe   | plain     | neutral - none      |  0.007 |   -0.010 |     0.027 | 0.748 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive - neutral  |  0.024 |    0.007 |     0.049 | 0.065 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | negative - neutral  |  0.007 |   -0.021 |     0.035 | 1.000 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | leveraged | positive - negative |  0.017 |   -0.010 |     0.049 | 0.372 | False     |  nan     |
| qwen2.5:14b          | xstest_unsafe | plain     | positive - neutral  | -0.003 |   -0.024 |     0.017 | 1.000 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | negative - neutral  | -0.014 |   -0.045 |     0.010 | 0.505 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | positive - negative |  0.010 |   -0.007 |     0.035 | 0.750 | True      |    1.000 |
| qwen2.5:14b          | xstest_unsafe | plain     | neutral - none      |  0.003 |   -0.028 |     0.035 | 1.000 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | positive - neutral  | -0.144 |   -0.267 |    -0.022 | 0.042 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | negative - neutral  |  0.200 |    0.067 |     0.322 | 0.010 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | leveraged | positive - negative | -0.344 |   -0.456 |    -0.233 | 0.000 | False     |  nan     |
| qwen3-vl:8b-instruct | secret        | plain     | positive - neutral  | -0.011 |   -0.089 |     0.078 | 1.000 | True      |    1.000 |
| qwen3-vl:8b-instruct | secret        | plain     | negative - neutral  |  0.289 |    0.189 |     0.389 | 0.000 | True      |    0.000 |
| qwen3-vl:8b-instruct | secret        | plain     | positive - negative | -0.300 |   -0.389 |    -0.200 | 0.000 | True      |    0.000 |
| qwen3-vl:8b-instruct | secret        | plain     | neutral - none      | -0.033 |   -0.144 |     0.078 | 0.706 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive - neutral  |  0.080 |    0.033 |     0.133 | 0.002 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | negative - neutral  | -0.037 |   -0.073 |    -0.003 | 0.060 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | leveraged | positive - negative |  0.117 |    0.063 |     0.173 | 0.000 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive - neutral  |  0.037 |   -0.003 |     0.077 | 0.109 | True      |    0.109 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | negative - neutral  | -0.060 |   -0.107 |    -0.017 | 0.011 | True      |    0.022 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | positive - negative |  0.097 |    0.057 |     0.143 | 0.000 | True      |    0.000 |
| qwen3-vl:8b-instruct | xstest_safe   | plain     | neutral - none      | -0.023 |   -0.060 |     0.010 | 0.268 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive - neutral  |  0.038 |    0.010 |     0.073 | 0.015 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | negative - neutral  |  0.007 |   -0.024 |     0.038 | 0.752 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | leveraged | positive - negative |  0.031 |    0.003 |     0.066 | 0.078 | False     |  nan     |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive - neutral  |  0.014 |   -0.003 |     0.038 | 0.369 | True      |    0.739 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | negative - neutral  | -0.007 |   -0.024 |     0.007 | 0.751 | True      |    0.751 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | positive - negative |  0.021 |    0.000 |     0.052 | 0.242 | True      |    0.727 |
| qwen3-vl:8b-instruct | xstest_unsafe | plain     | neutral - none      | -0.031 |   -0.062 |    -0.007 | 0.030 | False     |  nan     |

## Exploratory: non-refusal rate by harm category (plain request)

| model                | category                     |   none |   neutral |   positive |   negative |
|:---------------------|:-----------------------------|-------:|----------:|-----------:|-----------:|
| llama3.1:8b          | contrast_definitions         |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b          | contrast_discr               |  0.083 |     0.056 |      0.056 |      0.222 |
| llama3.1:8b          | contrast_figurative_language |  0.000 |     0.083 |      0.056 |      0.056 |
| llama3.1:8b          | contrast_historical_events   |  0.000 |     0.028 |      0.000 |      0.000 |
| llama3.1:8b          | contrast_homonyms            |  0.167 |     0.139 |      0.083 |      0.111 |
| llama3.1:8b          | contrast_privacy             |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b          | contrast_safe_contexts       |  0.111 |     0.167 |      0.000 |      0.000 |
| llama3.1:8b          | contrast_safe_targets        |  0.028 |     0.000 |      0.000 |      0.000 |
| llama3.1:8b          | definitions                  |  1.000 |     1.000 |      0.933 |      1.000 |
| llama3.1:8b          | figurative_language          |  1.000 |     1.000 |      1.000 |      0.933 |
| llama3.1:8b          | historical_events            |  1.000 |     1.000 |      0.933 |      1.000 |
| llama3.1:8b          | homonyms                     |  1.000 |     1.000 |      0.900 |      1.000 |
| llama3.1:8b          | nons_group_real_discr        |  0.933 |     0.833 |      0.967 |      0.967 |
| llama3.1:8b          | privacy_fictional            |  0.133 |     0.267 |      0.167 |      0.233 |
| llama3.1:8b          | privacy_public               |  1.000 |     1.000 |      0.967 |      1.000 |
| llama3.1:8b          | real_group_nons_discr        |  0.867 |     0.967 |      0.933 |      0.933 |
| llama3.1:8b          | safe_contexts                |  0.967 |     1.000 |      0.833 |      0.967 |
| llama3.1:8b          | safe_targets                 |  1.000 |     1.000 |      0.933 |      1.000 |
| llama3:8b            | contrast_definitions         |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3:8b            | contrast_discr               |  0.000 |     0.056 |      0.083 |      0.111 |
| llama3:8b            | contrast_figurative_language |  0.000 |     0.056 |      0.000 |      0.000 |
| llama3:8b            | contrast_historical_events   |  0.000 |     0.056 |      0.000 |      0.000 |
| llama3:8b            | contrast_homonyms            |  0.083 |     0.083 |      0.111 |      0.028 |
| llama3:8b            | contrast_privacy             |  0.000 |     0.000 |      0.000 |      0.000 |
| llama3:8b            | contrast_safe_contexts       |  0.056 |     0.194 |      0.167 |      0.000 |
| llama3:8b            | contrast_safe_targets        |  0.028 |     0.083 |      0.000 |      0.000 |
| llama3:8b            | definitions                  |  0.933 |     1.000 |      0.700 |      0.900 |
| llama3:8b            | figurative_language          |  1.000 |     1.000 |      0.933 |      1.000 |
| llama3:8b            | historical_events            |  0.967 |     1.000 |      0.933 |      1.000 |
| llama3:8b            | homonyms                     |  1.000 |     1.000 |      1.000 |      0.933 |
| llama3:8b            | nons_group_real_discr        |  0.667 |     0.800 |      0.867 |      0.700 |
| llama3:8b            | privacy_fictional            |  0.200 |     0.400 |      0.333 |      0.200 |
| llama3:8b            | privacy_public               |  1.000 |     1.000 |      1.000 |      1.000 |
| llama3:8b            | real_group_nons_discr        |  0.833 |     0.800 |      0.867 |      0.800 |
| llama3:8b            | safe_contexts                |  0.900 |     1.000 |      0.967 |      0.867 |
| llama3:8b            | safe_targets                 |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen2.5:14b          | contrast_definitions         |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b          | contrast_discr               |  0.222 |     0.139 |      0.194 |      0.167 |
| qwen2.5:14b          | contrast_figurative_language |  0.000 |     0.028 |      0.028 |      0.028 |
| qwen2.5:14b          | contrast_historical_events   |  0.083 |     0.028 |      0.000 |      0.000 |
| qwen2.5:14b          | contrast_homonyms            |  0.056 |     0.139 |      0.139 |      0.083 |
| qwen2.5:14b          | contrast_privacy             |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b          | contrast_safe_contexts       |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen2.5:14b          | contrast_safe_targets        |  0.000 |     0.056 |      0.000 |      0.000 |
| qwen2.5:14b          | definitions                  |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen2.5:14b          | figurative_language          |  1.000 |     1.000 |      1.000 |      0.900 |
| qwen2.5:14b          | historical_events            |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen2.5:14b          | homonyms                     |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen2.5:14b          | nons_group_real_discr        |  1.000 |     1.000 |      1.000 |      0.867 |
| qwen2.5:14b          | privacy_fictional            |  0.333 |     0.333 |      0.300 |      0.200 |
| qwen2.5:14b          | privacy_public               |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen2.5:14b          | real_group_nons_discr        |  0.833 |     0.900 |      0.867 |      0.900 |
| qwen2.5:14b          | safe_contexts                |  0.900 |     0.900 |      0.867 |      0.800 |
| qwen2.5:14b          | safe_targets                 |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen3-vl:8b-instruct | contrast_definitions         |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen3-vl:8b-instruct | contrast_discr               |  0.056 |     0.000 |      0.056 |      0.028 |
| qwen3-vl:8b-instruct | contrast_figurative_language |  0.000 |     0.000 |      0.056 |      0.000 |
| qwen3-vl:8b-instruct | contrast_historical_events   |  0.083 |     0.028 |      0.000 |      0.000 |
| qwen3-vl:8b-instruct | contrast_homonyms            |  0.111 |     0.056 |      0.083 |      0.000 |
| qwen3-vl:8b-instruct | contrast_privacy             |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen3-vl:8b-instruct | contrast_safe_contexts       |  0.083 |     0.000 |      0.000 |      0.000 |
| qwen3-vl:8b-instruct | contrast_safe_targets        |  0.000 |     0.000 |      0.000 |      0.000 |
| qwen3-vl:8b-instruct | definitions                  |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen3-vl:8b-instruct | figurative_language          |  0.767 |     0.767 |      0.900 |      0.667 |
| qwen3-vl:8b-instruct | historical_events            |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen3-vl:8b-instruct | homonyms                     |  1.000 |     1.000 |      1.000 |      1.000 |
| qwen3-vl:8b-instruct | nons_group_real_discr        |  0.967 |     0.933 |      1.000 |      0.867 |
| qwen3-vl:8b-instruct | privacy_fictional            |  0.500 |     0.300 |      0.533 |      0.267 |
| qwen3-vl:8b-instruct | privacy_public               |  1.000 |     1.000 |      0.967 |      1.000 |
| qwen3-vl:8b-instruct | real_group_nons_discr        |  1.000 |     0.933 |      1.000 |      0.867 |
| qwen3-vl:8b-instruct | safe_contexts                |  0.800 |     0.867 |      0.767 |      0.667 |
| qwen3-vl:8b-instruct | safe_targets                 |  0.900 |     0.900 |      0.900 |      0.767 |
