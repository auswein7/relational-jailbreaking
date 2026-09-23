# Model survey: which targets to test, and why

Phase 3 treats *how much refusal training a model has had* as a factor. The
targets below are grouped into tiers, with a directional prediction per tier
that is committed here before the run starts (H4 in `docs/DESIGN.md`).

Everything listed can run on this box (4x RTX A6000, 48 GB each) through
fairlib. Every target is a row in `relbreak/fairlib.yml` under a stable alias
(the identity every result carries); the tier, family, wave and status below
live in `relbreak/survey.yml` under the same alias, because a fairlib model
row describes how to build an adapter and nothing else. `python -m
relbreak.cli preflight --config <wave>` runs fairlib's chat-model conformance
suite over every alias before a wave starts. Two serving paths:

- **Ollama** (`provider: ollama`). Anything in the Ollama library, plus any
  GGUF repo on Hugging Face via `ollama pull hf.co/<org>/<repo>:<quant>`.
  Per-call seeds replay byte-identically, parallel serving, and several
  servers are used by running one process per server (`--ollama-host`).
- **Hugging Face transformers** (`provider: huggingface`, full weights).
  Usable for instruct models (`ministral_8b_hf`). Not usable for the
  base-model template factor: fairlib 0.6.4's adapter always applies the
  tokenizer's chat template and refuses `seed` and `stop`
  (`docs/ADOPTER_FINDINGS.md`), so base models are Ollama `-text` rows with a
  stop sequence and a caller-side transcript rendering (not written yet).

Disk is the binding constraint: 61 GB free (94% used). Q4_K_M pulls run 4-8
GB each, so Phase 3 is pulled and run in waves, removing models between
waves (`ollama rm`). The Hugging Face cache already holds ~200 GB of
weights, several of them directly relevant (see the "on disk" column).

## Tiers and predictions

| tier | what it means | prediction for the relational contrasts |
|---|---|---|
| **heavy** | current instruct models with explicit refusal training | Rapport tightens: emotional histories and named appeals lower compliance on benign-but-edgy prompts; no affirming increase (replicates Phase 2). |
| **light** | older or community chat tunes trained on helpfulness data without refusal data | Mixed, small. Baseline compliance on the harmful set is mid-range, so an affirming increase has room to show if it exists. |
| **none** | deliberately "uncensored" tunes with refusals removed | The codeword task is the only guardrail left. If rapport loosens instruction-following at all, it shows here first. |
| **base** | no assistant tuning; prompted through an explicit turn template | Behaves as a document continuer. Compliance tracks what the transcript genre predicts: a warm transcript predicts a warm, compliant continuation. This tier is where "how the user is encoded" (template) becomes a factor. |

The tiers order models by how much of their caution is a trained reflex.
The claim under test is that the sign of the relational effect flips
somewhere down this ladder.

## Candidates

Status: `local` = already pulled into Ollama; `hf` = full weights in the
Hugging Face cache (usable through the HF adapter, or by pulling a GGUF of
the same model into Ollama); `pull` = in the Ollama library, not on disk.

### Heavy safety tuning

| model | source | year | size | status | notes |
|---|---|---|---|---|---|
| llama3.1:8b, llama3:8b, qwen2.5:14b, qwen3-vl:8b-instruct | Ollama | 2024-25 | 5-9 GB | local | Phase 2 targets; the anchor for this tier. |
| gemma3:12b | Ollama `gemma3:12b` | 2025 | 8 GB | pull (hf: gemma-3-12b-it, 23 GB) | Strong refusal training, different lab. |
| llama2:7b-chat, llama2:13b-chat | Ollama | 2023 | 4 / 7 GB | pull | The canonical over-refuser (XSTest was written around it). Older generation; if any modern-vs-old difference exists it shows against llama3. |
| gpt-oss:20b | Ollama | 2025 | 14 GB | pull | Reasoning model with a strong policy layer; needs a large token budget like ornith. |
| Ministral-8B-Instruct-2410 | hf | 2024 | 15 GB | hf | Mistral's own safety-tuned generation, contrast to v0.1 below. |

### Light safety tuning

| model | source | year | size | status | notes |
|---|---|---|---|---|---|
| Mistral-7B-Instruct-v0.1 | hf (`mistralai/Mistral-7B-Instruct-v0.1`), or `hf.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF` | 2023 | 14 GB hf / 4 GB gguf | hf | Released with no moderation mechanism by the vendor's own description. Highest priority for this tier. |
| mistral:7b-instruct-v0.2 | Ollama | 2023 | 4 GB | pull | Same base, one iteration later; pairs with v0.1 and Ministral for a within-family ladder. |
| zephyr:7b-beta | Ollama | 2023 | 4 GB | pull | DPO on UltraFeedback, no safety data by design. |
| vicuna:13b-v1.5 | Ollama | 2023 | 7 GB | pull | ShareGPT tune of llama2; the first-generation "chat assistant" style. |
| openchat:7b-v3.5 | Ollama | 2023 | 4 GB | pull | C-RLFT tune, light moderation. |
| olmo2:7b | Ollama | 2024 | 4 GB | pull | Fully open training data. The one model whose post-training data can be searched for what relational language it saw. |
| Qwen2.5 0.5b / 1.5b / 3b / 7b instruct | hf (all four) or Ollama | 2024 | 1-15 GB | hf | Same recipe at four scales, plus the 14b already run: a scale series within one family. |

### No safety tuning

| model | source | year | size | status | notes |
|---|---|---|---|---|---|
| Dolphin3.0-Llama3.1-8B | hf, or Ollama `dolphin-llama3:8b` (Dolphin 2.9) | 2024-25 | 15 GB hf / 5 GB gguf | hf | Same base as llama3.1:8b with refusals removed: the cleanest paired comparison in the whole survey. |
| Dolphin3.0-Llama3.2-3B, Dolphin3.0-Qwen2.5-3B | hf | 2025 | 6 GB each | hf | Smaller uncensored tunes; pair with Qwen2.5-3B-Instruct. |
| nous-hermes:13b-llama2 | Ollama | 2023 | 7 GB | pull | Trained to never refuse. |
| llama2-uncensored:7b | Ollama | 2023 | 4 GB | pull | Refusals stripped from llama2. |
| wizard-vicuna-uncensored:13b | Ollama | 2023 | 7 GB | pull | Same idea, vicuna lineage. |

### Base models (no assistant tuning)

| model | source | size | status | notes |
|---|---|---|---|---|
| llama3.1:8b-text, llama3:8b-text | Ollama | 5 GB | pull | Base of two Phase 2 targets. |
| llama2:7b-text | Ollama | 4 GB | pull | Base of the llama2 chat and uncensored variants. |
| mistral:7b-text | Ollama | 4 GB | pull | Base of the Mistral instruct ladder. |
| qwen2.5:7b-base (and 0.5b-base etc.) | Ollama | 1-5 GB | pull | Base of the Qwen scale series. |

Base models need a template. Ollama applies no chat template to `-text`
tags, so the messages must be rendered into a transcript by the caller. The
plan is three renderings as a factor: the family's native chat tokens, a
plain `User:` / `Assistant:` transcript, and no delimiters (turns separated
by blank lines). The codeword task still works (the system text becomes a
preamble; the question is whether the continuation reveals it). The judge
tasks need a stop sequence at the next `User:` turn.

## Proposed waves

Each wave is one `configs/phase3*.yaml` listing aliases; pull, preflight,
run, analyze, remove. The `wave` field in `relbreak/survey.yml` records the
assignment.

1. **Paired families** (the strongest design): `llama31_8b` vs
   `dolphin_llama3` vs `llama31_8b_text`; `mistral_v01_q4` vs `mistral_v02`
   vs `ministral_8b_hf` vs `mistral_7b_text`; `llama2_7b_chat` vs
   `llama2_unc` vs `llama2_7b_text`. Nine models, ~45 GB at Q4.
2. **Light tier breadth**: `zephyr_7b`, `vicuna_13b`, `openchat_7b`,
   `olmo2_7b`, `nous_hermes_13b`. ~26 GB.
3. **Scale series**: `qwen25_05b`, `qwen25_15b`, `qwen25_3b`, `qwen25_7b`
   (`qwen25_14b` done) plus `qwen25_7b_text`. ~15 GB.
4. **Heavy tier additions**: `gemma3_12b`, `gpt_oss_20b`, `llama2_13b_chat`.
   ~30 GB.

Probe sets per tier: the JBB harmful set becomes primary again for light and
none tiers (their baselines are off the floor); XSTest safe stays primary for
heavy; the codeword task runs everywhere. Adding the leveraged appeal texts to
the `none` condition (no history) is part of every wave, so wording effects
are measured with no relationship present.

Cost: Phase 2 ran ~19k generations for four models in a few hours on two
Ollama servers. Wave 1 with three probe sets is ~45k generations, about a
working day of generation plus judging.

## Not candidates

- Anything needing a HF token or gated approval not already on disk.
- Models over ~30B (ornith 35B, Qwen3-30B-A3B, gemma-3-27b): serve fine as a
  second-rater judge but are slow as targets at the sample sizes here.
- gpt-oss-120b and Kimi-Linear-48B: config-only in the cache, no weights.
- TinyLlama AWQ/GPTQ: needs quantization runtimes that are not installed;
  `tinyllama:1.1b-chat` from Ollama is the substitute if a tiny model is
  wanted.
