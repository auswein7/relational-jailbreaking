# Adopter findings against fairlib 0.6.4

This repository is a deliberate stand-in for an outside adopter of fairlib.
Everything below was found while rebuilding `relbreak` on the 0.6.4 surface
(tag `v0.6.4`, 2026-09-23): each entry says what the adopter wanted, what
they had to do instead, and the fairlib change that would remove the
workaround. Line numbers refer to the tag. Entries marked **correct** are
places where the framework's refusal or omission is the right design and only
a docstring is missing. The list is ordered by how much it shaped this
repository, not by how hard it is to fix.

The companion `docs/FAIRLIB_INTEGRATION.md` says which seams the repository
now stands on and how.

## 1. One adapter, one bus, one budget (the finding that shaped the design)

`AbstractChatModel.bind_event_bus` stores a single bus and replaces silently
(`core/interfaces/llm.py:632-656`); `SimpleAgent.__init__` rebinds the
model to its own bus on every construction (`modules/agent/simple_agent.py:252`);
`ModelManager.get_model` hands the same cached adapter to every caller
(`modules/mal/model_manager.py:153`); `bind_cost_budget` refuses a second
budget on the same adapter (`llm.py:654-673`). So with one cached adapter and
four concurrent agents, every `ModelInvocationEvent`, the summarizer's
included, lands on whichever run's bus was bound last, and a per-run token
ceiling is impossible. `ToolExecutor` refuses the same mistake with a
`ConfigurationError` (`simple_agent.py:236-247`); adapters do not.

What relbreak does: one process-wide bus bound once to every adapter
(`relbreak/observe.py`), a `ContextVar` set per run, and a router that
forwards each event to that run's `TraceRecorder`. `SimpleAgent`'s rebinding
is then to the same object. Budgets are per stage, not per run.

Proposed: carry the bus (and the budget) in a `contextvars.ContextVar` set by
`SimpleAgent.arun` and read by `_invocation`, with `bind_event_bus` as the
fallback; or refuse (as the executor does) when an agent would rebind an
adapter already bound to a different bus; and let `ModelManager(app_settings,
*, events=None)` bind every adapter it builds. The `SimpleAgent` docstring
should say that a shared model implies a shared bus.

## 2. Observation

- **`ModelInvocationEvent` carries accounting, never content**
  (`core/events.py:503-538`). A bare `ainvoke` with a bus bound emits model
  name, provider, duration, outcome, usage and a request digest; no messages,
  no reply text, no options, no seed. An adopter running a model study outside
  an agent keeps the text out of band and correlates by digest, which is what
  `relbreak/observe.py:Ledger` does. Proposed: an opt-in content-bearing
  `ModelExchangeEvent(request, reply, options)`, or at least carry the checked
  generation options on the existing event (they are provider-neutral by
  construction); and add `step` and `source` (planner / summarizer / validator
  / direct) so the summarizer's call is distinguishable from the planner's.
- **`reserved_usd` is documented as the USD reserved for the call but is
  always 0.0 on the emitted event** (`events.py:529-538` vs
  `core/model_invocation.py:376-378`, CHANGELOG 0.6.4).
- **`TraceRecorder`'s traced set is a private constant with no constructor
  argument** (`core/trace.py:44-66`) and omits `DegradedResponseEvent`,
  `UnverifiedCompletionEvent`, `LifecycleHookEvent`, `BudgetExceededEvent`,
  `CapabilityDeniedEvent`, `NetworkEgressDeniedEvent` and the planner recovery
  events. relbreak subscribes those to `recorder.record` by hand and keeps its
  own copy of the tuple (`relbreak/observe.py:TRACED_TYPES`). Proposed:
  `TraceRecorder(bus, *, event_types=DEFAULT_TRACE_EVENT_TYPES)` with the
  default exported, and the typed-failure events in the default.
- **`AgentRunTrace` has `to_dict`/`save` but no `from_dict`/`load`**
  (`trace.py:87-130`), unlike `Message`, `Usage`, `SessionRecord` and
  `AgentCheckpoint`; the analysis stage re-reads JSON as untyped dicts.
- **A Pydantic `tool_input` serializes as `repr`** in a trace payload because
  `_to_trace_payload` checks `to_dict` but not `model_dump`
  (`trace.py:215-245`), while `ToolCallPreEvent.tool_input` is documented as
  possibly a Pydantic model.
- **Subscribing to `FairlibEvent` receives nothing, silently**
  (`core/event_bus.py:75`, exact-type dispatch). Proposed: raise
  `EventBusError` on a base class, or document the enumerable public tuple.
- **`TraceRecorder` and `arun_with_trace` appear in no doc page**, only in a
  demo and the CHANGELOG; the previous version of this repository hand-rolled
  a serializer because the shipped one was not discoverable.

## 3. Security and the shell

- **`allowed_egress` does not govern `ShellTool`.** The egress allowlist is
  consulted only for tools that declare `network_egress` or `reaches_network`
  (`modules/action/executor.py:595-744`); `ShellTool` declares neither. A
  shell command is screened by `validate_input`, which in
  `BasicSecurityManager` is three prompt-injection regexes
  (`modules/security/basic_security_manager.py:58-66,312-334`). Verified live
  on the tag: `curl`, `rm -rf fixtures` and `cat /etc/hostname` all run under
  `BasicSecurityManager(allowed_egress=[])`; `echo the following text` is
  refused. The previous version of this repository claimed "no network
  egress" on that basis; the claim was false. relbreak now implements
  `AbstractSecurityManager` (`relbreak/agentic/security.py`) with a
  program-name denylist. Proposed: (a) the `allowed_egress` docstring should
  say "declared-egress tools only"; (b) a typed shell policy seam,
  `AbstractSecurityManager.validate_command(command) -> None` raising a typed
  `CommandDeniedError`, called by `ShellTool` instead of `validate_input`,
  with `BasicSecurityManager(allowed_commands=...)`. Today `validate_input`
  is overloaded: the same check screens shell commands and every tool's JSON
  input (`executor.py:288`), so an adopter's shell policy has to guess which
  inputs are commands by shape.
- **No typed exit code reaches the consumer.** The executor renders
  `ShellResult` to a string and drops it (`executor.py:370-379`);
  `ToolCallResult` and `ToolCallPostEvent` carry `observation: str` only.
  relbreak parses `(exit N)` out of the rendering (`relbreak/agentic/sandbox.py`).
  Proposed: `output: Optional[ToolOutput]` on the result and the event.
- **`ShellTool` inherits the harness environment and has no per-instance
  timeout** (`builtin_tools/shell_tool.py:114-142`); the timeout comes only
  from `limits.shell.default_timeout_seconds`, which ships as 0 = none.
  relbreak sets the limit in its settings document and prepends the venv to
  `PATH` in the CLI. Proposed: `ShellTool(root, security, *, timeout=None,
  env=None)`.
- **No conformance suite for a security manager** (`fairlib/conformance/`
  covers tools and chat models). An adopter implementing the ABC cannot prove
  it refuses what it says.
- **`GraphingTool.required_capability` is `"filesystem_write"`** while the
  rooted tools use `"filesystem.write"` (`graphing_tool.py:60` vs
  `_rooted_file_tool.py:136`); a bag that grants one does not grant the other.
- The bounded-subprocess seam on the working branch (`core/sandbox.py`,
  `IsolationLevel`, `compute_bounds=`) is past the tag and, by its own
  docstring, not a network sandbox. Its CHANGELOG entries sit under `[0.6.4]`
  on that branch and should move to `[Unreleased]`.

## 4. Memory, sessions, grounding

- **`SummarizingMemory` never compacts `history[0]`** (`modules/memory/summarization.py:455,958`)
  because it assumes a system prompt sits there, but `SimpleAgent` never
  stores one in memory. In this study that made the first relational turn,
  the warmest or coldest wording, survive every compaction verbatim in both
  the compacted and restored tiers. relbreak now opens every session with a
  neutral, unwrapped task so the reserved slot carries no valence. Proposed:
  reserve index 0 only when `history[0].role == "system"`, and document it.
- **The compaction prompt is hard-coded** (`summarization.py:882-892`) and
  the summarizer call passes no generation options and is never bound to the
  memory's bus (`summarization.py:895`), so the write is neither variable nor
  reproducible from a seed. relbreak builds a second adapter for the same row
  with persisted `options={seed, temperature, max_tokens}` through the model
  manager (`relbreak/models.py:variant`). Proposed: a `summarizer` component
  seam (or `summary_prompt=` and `summarizer_options=`), and bind the bus.
- **Compaction re-fires on every read once the message count is over the
  limit** (`summarization.py:387-389`, read at every agent step). With a
  message-count trigger the compacted history was re-summarised on nearly
  every probe step. The token trigger (`max_context_tokens`) is the
  documented answer and is what relbreak uses now; the `max_history_length`
  docstring should say this.
- **The summary body has no public path.** `SUMMARY_BODY_KEY`,
  `SUMMARY_MARKER_KEY` and `RE_GROUND_MARKER_KEY` (`core/message.py:42-49`)
  and the banners in `modules/memory/_compaction_text.py` are not exported;
  relbreak deep-imports them to strip the banner. Proposed:
  `MemorySummarizedEvent.summary_body`, or export a helper.
- **No boot-time or per-step grounding seam.** `PathArtifactReGrounder`
  fires only after a compaction; `PreModelHookContext.history` is read-only;
  `SimpleAgent` and `PromptBuilder` take no context provider. The previous
  version of this repository called `refresh()` by hand as a file reader and
  the model saw its own notes labelled "untrusted file content". relbreak now
  pins a plain user message. Proposed: `ground_on_start=True` on
  `SummarizingMemory`, or a grounded-artifacts section on `PromptBuilder`.
- **No memory-notes write seam and no notes store.** fairlib ships nothing
  like Claude Code's auto memory or OpenClaw's `MEMORY.md`; the memory-file
  tier is entirely application code (`relbreak/agentic/memory_tiers.py:NOTES_PROMPT`).
  Proposed, if a second adopter needs it: `AbstractMemoryWriter.awrite(history)
  -> str` with a `MemoryWrittenEvent`.
- **`restore_agent` assigns `memory.history` directly** (`core/session.py:463-470`)
  instead of going through the memory; a memory's own invariants (the pinned
  counter) resync only on the compaction path. Proposed:
  `AbstractMemory.replace_history(messages)` with a refusing default.
- **`SummarizingMemory.get_history()` degrades** to a `"...summary..."`
  placeholder on an over-limit sync read (`summarization.py:626-634`) instead
  of refusing.
- **`FaissVectorStore` persists to a shared default directory on every add**
  (`vector_faiss.py:100,198-219`); under concurrency that is a race. relbreak
  gives each run its own directory. Proposed: `persist: bool` or
  `index_dir=None` for in-memory; and let `InMemoryVectorStore` take an
  embedder so the shipped in-memory store computes a real similarity.
- `SimpleRetriever.retrieve` defaults `top_k=2`, `aretrieve` 5, the ABC 5.
- The ABC declares `status` required on `save`/`save_agent`; the concrete
  store defaults it.
- **`SessionRecord` carries no memory type** (`session.py:53-64`): correct,
  memory is a component the fresh agent is configured with, but
  `restore_agent` should say so.
- No `AbstractMemory` conformance suite.

## 5. Model manager, settings, adapters

- **`ModelSettings` drops unknown keys silently** (`core/config_schemas.py:35-51`,
  no `extra="forbid"`; contrast `SecuritySettings`). A `tier:` on a row
  vanishes. relbreak keeps tier metadata in `relbreak/survey.yml` keyed by
  alias and cross-checks the two files. Proposed: `extra="forbid"`, plus one
  docstring line saying adopter metadata belongs in the adopter's own file.
- **`AppSettings` and `ModelSettings` are not exported** although
  `ModelManager.__init__` is annotated with `AppSettings`.
- **`HuggingFaceAdapter` cannot bypass or override the chat template**
  (`huggingface_adapter.py:785-824`, with a broad-except fallback to a fixed
  join) and **refuses `seed` and `stop`** (`:1124,1153-1155`) although
  transformers can honor both. The survey's base-model template factor is
  therefore Ollama-only. Proposed: a `chat_template` constructor argument
  (None, Jinja string, or callable) declared in the description, and `seed`
  under the existing generation lock plus `stop` via `stop_strings`.
- **`LoadBalancerAdapter` is a client for a separate vLLM manager service**,
  not a balancer over adapters; two Ollama hosts behind one alias is not
  expressible. relbreak drains one queue from one process per host.
  **Correct**: host affinity is a deployment fact; alias-per-host and
  settings-per-process express it.
- **`_PROVIDERS` is private** (`model_manager.py:40-56`); an adopter's own
  `AbstractChatModel` cannot be a `provider:` row. Proposed:
  `ModelManager.register_provider(name, factory)`.
- **The adapter cache has no release** and `OllamaAdapter` never closes its
  `httpx.AsyncClient` (`local_llama_adapter.py:121-170`); one process per
  wave is the workaround. Proposed: `ModelManager.release(alias)` and an
  optional `aclose()` on the adapter contract.
- **`describe_config()` omits `timeout`** on Ollama and HF, and the HF
  load-time kwargs (`device_map`, `dtype`); the run manifest reads them from
  the settings row instead.
- **Ollama 404 (model not pulled) classifies as `Kind.UNKNOWN`**
  (`errors.py:367-382`); the preflight conformance run catches it, but the
  kind should be actionable.
- **`LLMSettings.timeout` cannot be None and has a floor of 10**
  (`config_schemas.py:199`); per-row `kwargs.timeout` is the override, which
  the packaged settings comment should say.
- **The conformance demo reaches private adapter state** for its
  `recorded_request` hook (`demos/demo_chat_model_conformance.py:88-110`);
  over Ollama an adopter cannot run `system_message_delivery`,
  `stateless_calls` or `output_budget_accepted` without a transport double.
- `ModelManager` cannot take a bus (see section 1).
- `fairlib.__version__` reads install metadata and reported 0.6.3 for the
  0.6.4 checkout until the editable install was refreshed; a source-tree
  fallback would spare the manifest a wrong version.
- `demos/demo_model_comparison.py` says it builds models from settings and
  then hand-constructs two adapters.

## 6. Orchestration, budget, reliability

- **The orchestration contract and concretes are not exported**
  (`FileWorkQueue`, `AbstractWorkQueue`, `JobRecord`, `JobStatus`,
  `OrchestrationLimits`), by documented decision; relbreak deep-imports them
  (`relbreak/work.py`). The contract types at least belong on the surface,
  since a networked queue implements them.
- **`CheckpointWorkRunner` binds the unit of work to a pre-built
  `agent.arun`** (`modules/orchestration/runner.py:53-55,224-225`); an
  adopter whose job builds its own agent, sandbox and memory per payload
  writes the claim / renew / complete loop itself (about sixty lines in
  `relbreak/work.py`). Proposed: accept `agent_factory: Callable[[JobRecord],
  BaseAgent]` or `work: Callable[[JobRecord], Awaitable[None]]`.
- **The runner never releases a retryable `DegradedResponse`**
  (`runner.py:124-147` completes every `FairlibError` as failed) although
  TIMEOUT / CONNECTION / RATE_LIMIT / SERVER_ERROR are `retryable=True`.
- **`claim()` ignores `restart_backoff_seconds`** (verified: 0.17 s re-claim
  after a 5 s backoff) and a dead-letter reason can be the previous attempt's
  error (`queue.py:516`).
- **`job_id` charset rejects natural keys** (`queue.py:51`): **correct** (it
  is a filename); document "hash your key".
- **The token meter wears a USD costume.** `CostRates(1.0, 1.0)` makes the
  budget count tokens exactly (verified), but every field, error and event
  says USD. Proposed: a `token_ceiling=` spelling or a docstring line.
- **No validator or retry seam on a bare `ainvoke`**; the judge's
  parse-or-retry loop lives in the consumer (`relbreak/judge.py:invoke_with_retry`).
  relbreak wraps the judge as an `AbstractTool` so at least the failure is
  typed and the conformance suite covers it.
- **`CallDeadlineError` is a conformance-harness error exported as if it
  were a runtime deadline** (`conformance/tools.py:233`); the runtime signal
  is `DegradedResponse(kind=TIMEOUT)`.
- **Lifecycle hooks have no post-model point**, so a hook cannot observe
  model output; `LifecycleHookEvent` is not in the default trace set.
- `modules/learning` is a 25-line substring `ModelSelector` and
  `modules/research/eval` has no Python files.
- `demos/demo_orchestration_layer.py` subclasses `SimpleAgent` to model a
  crash, which the framework's own rules tell adopters never to do.
- No `AbstractWorkQueue` conformance suite.

## 7. Agent, planner, prompts, config documents

- **`OllamaAdapter` declares `max_context_window=None`** even when its
  options set `num_ctx` (`modules/mal/local_llama_adapter.py:452`), so
  `ModelCapabilities` cannot answer "how long is this model's window" and
  `_check_context_window_usage` never warns. Ollama also truncates an
  overfull prompt from the front with no error (verified on 0.33.1: a
  3,815-token prompt at `num_ctx` 2048 was served as 1,915 tokens), so an
  adopter learns of it only by comparing `usage.prompt_tokens` against what
  was sent. relbreak reads `num_ctx` off the model row and checks the served
  count on every Phase 5 probe. Proposed: report `num_ctx` (or the model's
  trained length from `/api/show`) as `max_context_window`, and a typed
  refusal or a degraded flag when the served prompt is shorter than the
  request.
- **Lifecycle hooks see the planner's raw `tool_input`, typed `Any`**
  (`core/interfaces/lifecycle_hooks.py:103,119`). With `SimpleReActPlanner`
  it is the unparsed JSON string, not the tool's validated input model, and
  nothing documents which. relbreak's enforced arm read `path` off a dict,
  so the Rule 3 and Rule 6 vetoes (edits to a test, to AGENTS.md) never
  fired and a 2026-09-24 pilot counted five enforced-arm test weakenings
  with no veto; `hooks.py` now parses the string itself. A hook that guards
  arguments needs the same input the tool will receive. Proposed: pass the
  validated input (or a parsed `tool_args`) on both hook contexts, and
  document the field's type.
- **In-place mutation of `planner.prompt_builder` works only before the
  first plan** (`base_text_planner.py:300-309,350-358`); the sanctioned shape
  is to construct a `PromptBuilder` and pass `prompt_builder=`, which relbreak
  now does. **Correct**, the docstring says so; the demo is the reference.
- **`date_context` is on by default**, so the system prompt changes daily
  and a seeded run does not replay (`core/prompts/builders.py:186-191`);
  relbreak sets `builder.date_context = None`. Proposed: a constructor flag
  and a line in the config-document docs.
- **`AgentFactory` builds tools with `cls()`** (`modules/agent/factory.py:647`),
  so rooted tools need zero-argument closures; and the config document has no
  memory, security, generation-option or seed section, and no
  `max_parse_attempts`. An arm is a document plus a consumer manifest, not a
  document plus a seed.
- The `arun` docstring says two parse attempts; the constructor takes
  `max_parse_attempts`.
- The planner recovery events (`PlannerKvFallbackEvent` and four more),
  `ShellResult`, `ShellInput`, `GENERATION_OPTION_NAMES` and `plain_data` are
  not exported; a custom adapter needs `GENERATION_OPTION_NAMES` to declare
  truthful capabilities (this repository's test double does).

## 8. Documentation and precedent

- The README on release day still pins `fair-llm==0.6.3` in two places,
  lists a PDF that does not exist, promises an `mcp:` block the packaged
  settings lack, and gets a model by hand-constructing an adapter;
  `ModelManager` appears only in the demo list and the event bus, the trace
  recorder and sessions appear nowhere in its text.
- There is no adopter guide. The Guide PDF is v0.2.1 and names none of
  `ModelManager`, `AgentEventBus`, `TraceRecorder`, `JsonSessionStore`,
  `FAIR_LLM_SETTINGS` or `configure_settings`; the canonical 0.6.4 path exists
  only in the CHANGELOG, docstrings and demos. Proposed: one
  `docs/ADOPTER_GUIDE.md` whose python blocks the existing docs-audit test
  holds to the public surface: `configure_settings` -> `ModelManager` ->
  `AgentEventBus` + `events=` -> `arun_with_trace` -> `JsonSessionStore`.
- The only environment variable fairlib reads is `FAIR_LLM_SETTINGS`; the
  `FAIR_LLM_PROVIDER` / `FAIR_LLM_OLLAMA_HOST` family in `fair_llm_tutor` is
  that repository's own and reads as fairlib's to a newcomer.
- No in-workspace consumer uses `ModelManager`, `configure_settings` or
  `TraceRecorder`; `fair_llm_tutor` and `fair_prompt_optimizer` each carry a
  hand-rolled provider ladder, the exact thing the manager's demo says it
  removes. This repository is the first adopter of those three seams.

## Candidate issues, in order

1. Adapter-scoped bus and budget with silent rebinding (section 1).
2. `allowed_egress` and the shell: docstring plus a typed command policy seam;
   typed exit code on the tool event (section 3).
3. `SummarizingMemory`: immortal first message; seedable, observable,
   configurable summarizer; summary body on the event (section 4).
4. `TraceRecorder`: configurable and complete traced set; `from_dict`;
   Pydantic payloads (section 2).
5. `ModelSettings` `extra="forbid"`; export `AppSettings` / `ModelSettings`,
   the orchestration contract, `GENERATION_OPTION_NAMES`, `plain_data`
   (sections 5, 6, 7).
6. `CheckpointWorkRunner` work factory; release retryable degraded
   responses; honor backoff (section 6).
7. HF adapter: template seam, `seed`, `stop` (section 5).
8. Adopter guide page held by the docs-audit test; README fixes (section 8).
9. Lifecycle hook contexts: pass the validated tool input and document the
   `tool_input` type (section 7).
10. Ollama: declare `max_context_window` from `num_ctx`; surface silent
    prompt truncation (section 7).
