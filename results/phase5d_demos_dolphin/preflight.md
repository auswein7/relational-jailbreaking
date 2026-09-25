# phase5d_demos_dolphin: model conformance

```
dolphin3_8b_128k: conforms
  passed  declared_surface: all seven contract methods present
  passed  describe_config: OllamaAdapter / dolphin3:8b
  passed  capabilities: declares streaming
  passed  token_estimate: 1 for one word, 250 for 200
  passed  ainvoke_returns_assistant_message: 5 chars of content
  skipped system_message_delivery: no recorded_request hook to observe the payload
  skipped stateless_calls: no recorded_request hook to observe the payload
  skipped vision_image_handling: no vision sample to send
  passed  usage_reporting: usage surfaced on the reply (prompt_tokens=27, completion_tokens=3, done_reason=stop)
  skipped output_budget_accepted: no recorded_request hook to observe the payload
  passed  generation_option_handling: carries frequency_penalty, max_tokens, presence_penalty, seed, stop, temperature, top_k, top_p; every other neutral option is refused typed
  passed  model_invocation_event: one event per call for ollama/dolphin3:8b
  skipped sync_async_parity: responses are not deterministic on this transport
  skipped streaming_consistency: responses are not deterministic on this transport
  skipped typed_failure: no failure_mode hook to observe the error channel
  passed  model_capability_gating: denied foreign model; allowed 'dolphin3:8b'
  passed  ainvoke_cooperates_with_the_loop: 27 ms, 4 loop tick(s) during the call

judge: conforms
  passed  declared_surface: all seven contract methods present
  passed  describe_config: OllamaAdapter / qwen2.5:14b
  passed  capabilities: declares streaming
  passed  token_estimate: 1 for one word, 250 for 200
  passed  ainvoke_returns_assistant_message: 4 chars of content
  skipped system_message_delivery: no recorded_request hook to observe the payload
  skipped stateless_calls: no recorded_request hook to observe the payload
  skipped vision_image_handling: no vision sample to send
  passed  usage_reporting: usage surfaced on the reply (prompt_tokens=26, completion_tokens=2, done_reason=stop)
  skipped output_budget_accepted: no recorded_request hook to observe the payload
  passed  generation_option_handling: carries frequency_penalty, max_tokens, presence_penalty, seed, stop, temperature, top_k, top_p; every other neutral option is refused typed
  passed  model_invocation_event: one event per call for ollama/qwen2.5:14b
  skipped sync_async_parity: responses are not deterministic on this transport
  skipped streaming_consistency: responses are not deterministic on this transport
  skipped typed_failure: no failure_mode hook to observe the error channel
  passed  model_capability_gating: denied foreign model; allowed 'qwen2.5:14b'
  passed  ainvoke_cooperates_with_the_loop: 429 ms, 83 loop tick(s) during the call
```
