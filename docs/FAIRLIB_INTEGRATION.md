# How relbreak stands on fairlib

`relbreak` is a layer-4 consumer of fairlib 0.6.4 and adds nothing to the
framework. This page maps every fairlib seam the repository uses to the code
that uses it, and records the seams that were considered and left alone. The
frictions met on the way are in `docs/ADOPTER_FINDINGS.md`.

Every name below imports from `fairlib`; the four deep imports the repository
still carries are listed at the end.

## Settings and models

| what | fairlib seam | where in relbreak |
|---|---|---|
| one settings document for the whole study | `configure_settings(path)` at package import, honoring `FAIR_LLM_SETTINGS` when set | `relbreak/__init__.py`, `relbreak/fairlib.yml` |
| every survey target and judge as a configured row | `AppSettings.models` (`ModelSettings`: provider, model_name, temperature, max_tokens, kwargs) | `relbreak/fairlib.yml`: one alias per model; judge rows pin their own `kwargs.host` |
| resolving an alias to an adapter, cached, provider-agnostic | `ModelManager(settings).get_model(alias)` | `relbreak/models.py:get` |
| the same row with persisted generation options (a seeded summarizer) | `ModelManager` over a copy of the settings with a derived row | `relbreak/models.py:variant` |
| per-process host affinity (several Ollama servers) | `kwargs.host` on the row, filled per process before the first `get_model` | `relbreak/models.py:set_ollama_host`, CLI `--ollama-host` |
| caps fairlib components read at construction | `limits.memory.max_summary_chars`, `limits.shell.*`, `llm.timeout` | `relbreak/fairlib.yml` |
| model provenance in the run manifest | `describe_config()` -> `ModelDescription`, plus the row and the survey entry | `relbreak/models.py:describe`, `relbreak/experiment.py:write_manifest` |
| is every alias pulled and contract-conformant before a wave | `check_chat_model_conformance(ChatModelConformanceCase(...))` | `relbreak/models.py:preflight`, CLI stage `preflight` |
| per-call determinism | the neutral generation options (`seed`, `temperature`, `max_tokens`, `stop`) on `ainvoke` and on `SimpleAgent.arun(generation_options=)` | `relbreak/llm.py:chat`, `relbreak/agentic/experiment.py:_options` |

What fairlib cannot carry lives beside it: tier, family, wave, status and
role per alias in `relbreak/survey.yml`, cross-checked at load
(`relbreak/models.py:validate_run_config`).

## Observation

| what | fairlib seam | where in relbreak |
|---|---|---|
| one bus for the process, every component on it | `AgentEventBus`; `events=` on `SimpleAgent`, `ToolExecutor`, `SummarizingMemory`, `FileWorkQueue`, `CostBudget`; `bind_event_bus` on adapters | `relbreak/observe.py:BUS`, `relbreak/observe.py:bind` |
| a run's typed trace | `TraceRecorder(bus, run_id=, metadata=)`, `record`, `finish`, `AgentRunTrace.save` | `relbreak/observe.py:run_trace`; traces under `data/raw/<run>/traces/` |
| attributing events to concurrent runs on one bus | a `ContextVar` set per task; a single subscriber routes to the run's recorder | `relbreak/observe.py:_route` |
| accounting for every model call in phases 1-3 (no agent) | `ModelInvocationEvent` (model, provider, duration, outcome, usage, request digest) | `relbreak/observe.py:Ledger` -> `data/raw/<run>/invocations.jsonl` |
| token usage and truncation per reply | `Message.usage` (`Usage`: prompt/completion tokens, `done_reason`) | `relbreak/llm.py:usage_dict`; stored on every response row |
| what the model saw | `planner.capture_prompt_configuration()` (`PromptCapture`) | `relbreak/agentic/agent.py:provenance`, in every build trace's metadata |
| the compaction write as data | `MemorySummarizedEvent(dropped, kept, summary, reason)` | in the probe trace; `relbreak/agentic/sandbox.py:accounting` counts them |
| a run that raised at a fairlib boundary | `FairlibError` subclasses; `DegradedResponseEvent`, `UnverifiedCompletionEvent`, `BudgetExceededEvent`, `LifecycleHookEvent` routed to the recorder | `relbreak/observe.py:TRACED_TYPES` |

The bus never carries model text (`ModelInvocationEvent` is accounting only).
The text is the return value of the call and lands in the run's JSONL row;
the digest ties the row to the event.

## Stage execution

| what | fairlib seam | where in relbreak |
|---|---|---|
| a durable, resumable, multi-process job store per stage | `FileWorkQueue` (leased atomic claims under a POSIX lock, renew, complete, release, dead-letter, quarantine) with `OrchestrationLimits` | `relbreak/work.py:enqueue`, `drain`, `run_stage` |
| retry policy | `DegradedResponse.retryable` -> release; other `FairlibError` -> a result row with an error; anything else -> release, `max_attempts=3` | `relbreak/work.py:drain` |
| lifecycle observability | `JobClaimedEvent` and the other `Job*` events on the process bus | `FileWorkQueue(events=observe.BUS)` |

The queue holds only the lifecycle; results stay in the stage's JSONL file
(`relbreak/work.py:read_keyed`, last row per key wins).

## The agent (Phase 4)

| what | fairlib seam | where in relbreak |
|---|---|---|
| the agent | `SimpleAgent` over `SimpleReActPlanner` (the planner for small local models) | `relbreak/agentic/agent.py:build` |
| the system prompt, frozen | `PromptBuilder` with `RoleDefinition`, `date_context = None`, passed as `prompt_builder=` | `relbreak/agentic/agent.py:prompt_builder` |
| tools | `ListDirTool`, `GlobTool`, `GrepTool`, `ReadFileTool`, `EditFileTool`, `WriteFileTool` (root-confined by fairlib), `ShellTool` | `relbreak/agentic/agent.py:build_tools` |
| containment of the shell | `AbstractSecurityManager` implemented: `validate_input` denies network, privilege and package-manager programs; egress always refused | `relbreak/agentic/security.py:SandboxShellPolicy`; timeout from `limits.shell` |
| the enforced control arm | `AbstractLifecycleHooks` implemented: `pre_tool` vetoes the six rules, `post_tool` tracks a green test run; `SimpleAgent(lifecycle_hooks=)` | `relbreak/agentic/hooks.py:RuleEnforcingHooks` |
| a token ceiling per stage | `CostBudget(rates=CostRates(1.0, 1.0), session_usd_ceiling=tokens)` bound by `SimpleAgent(budget=)`; a refusal is a typed `BudgetExceededError` | `relbreak/agentic/experiment.py:_budget` (off by default) |
| parse failures as typed failures | `PlannerParseError` with `raw_output`; `max_parse_attempts` | probe rows keep `error` and `raw_output` |

## Memory tiers (Phase 4)

| tier | fairlib seam | where in relbreak |
|---|---|---|
| transcript | `WorkingMemory` | `relbreak/agentic/memory_tiers.py:working` |
| compacted | `SummarizingMemory(llm=<seeded variant>, max_context_tokens=, overhead_token_count=, messages_to_keep_at_end=, events=BUS)`; the summary located by its marker | `memory_tiers.py:compact` |
| restored | the compacted output saved with `JsonSessionStore.save(..., status=SessionStatus.COMPLETED)` and put into the fresh agent with `restore_agent` | `memory_tiers.py:build` (`after_build`) |
| memory file | application code (fairlib ships no notes writer); the notes pinned as a `Message(importance="pinned")` | `memory_tiers.py:NOTES_PROMPT` |
| retrieved | `LongTermMemory` over `FaissVectorStore(SentenceTransformerEmbedder)`, `SimpleRetriever.retrieve` | `memory_tiers.py:build`, `_vector_store` (per-run index directory) |
| the built history itself | `JsonSessionStore.save_agent(key, agent, status=)` after the build; `load(key).messages` before the probe | `relbreak/agentic/experiment.py` |

## The judges

| what | fairlib seam | where in relbreak |
|---|---|---|
| a one-shot judge with typed input, typed output and typed failure | `AbstractTool` with Pydantic `input_schema` / `output_schema`, `SideEffect.EXTERNAL`, `reaches_network`, `network_egress` derived from the judge adapter's host; `tool.invoke` validates the input | `relbreak/judge.py:LabelJudgeTool`, `RatingJudgeTool` |
| the judge tool's contract, checked | `acheck_tool_conformance(ToolConformanceCase(...))` in the test suite | `tests/test_fairlib_integration.py` |
| the second rater | the same tool over another alias (`--judge-model`) | CLI `audit` stage |

## Considered and not used

- `CheckpointWorkRunner`: its unit of work is a pre-built agent's `arun`;
  every relbreak job builds its own sandbox, memory and agent.
- `arun(validator=, max_retries=)`, `ActionVerifier`, `ResponsePool`: each
  feeds text back to the model or cycles wording, which would change the
  treatment. `UnverifiedCompletionEvent` is traced instead.
- `LoadBalancerAdapter`: a client for a separate vLLM service, not a
  balancer over Ollama hosts.
- `HuggingFaceAdapter` for base models: no template override, no `seed`, no
  `stop`; the base tier is Ollama `-text` rows until that changes.
- `AgentFactory` / `save_agent_config`: the document cannot carry memory,
  security, generation options or the seed, so an arm would be a document
  plus a manifest; the trace metadata already carries the `PromptCapture`
  and the model description.
- `build_worker_manager` / `WorkerAgentTool` committees: a manager-decides
  pattern, wrong for a blind judge and a second rater.
- `CapabilityBag`: confines file tools that the rooted tools already
  confine, and cannot see shell paths.
- `PathArtifactReGrounder` for the memory file: a post-compaction reader
  that labels the file untrusted; the notes are operator-owned context.
- MCP, `fairlib.chaos`, `GroundedContextBuilder` / citation grounding: no
  fit for this study.

## Remaining deep imports

Four names the repository needs are not on the public surface:

- `fairlib.core.message.SUMMARY_BODY_KEY` and the two banners in
  `fairlib.modules.memory._compaction_text` (to read the summary body);
- `fairlib.core.generation_options.GENERATION_OPTION_NAMES` (the test
  double's capability record);
- `fairlib.core.interfaces.orchestration` and
  `fairlib.modules.orchestration` (the work queue; unexported by decision).
