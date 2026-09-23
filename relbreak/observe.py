"""Observation by subscription: one process-wide AgentEventBus, run-tagged.

Every adapter relbreak resolves is bound to BUS once, and every fairlib
component built here (agents, executors, memories, security managers) is
handed BUS. A run declares itself with run_trace(run_id, ...); while that
context is active, every event the framework emits from that task is routed
to the run's TraceRecorder, and the result is a fairlib AgentRunTrace saved
next to the run's outcome. A ContextVar carries the run id, so concurrent
runs on one bus (and on one cached adapter) do not cross-talk.

The bus never carries model text: ModelInvocationEvent is accounting only
(model, provider, duration, outcome, usage, request digest). The text is the
return value of the call and lands in the run's JSONL row; the digest ties
the row to the event.
"""

from __future__ import annotations

import json
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import UTC, datetime
from pathlib import Path

from fairlib import (
    AbstractChatModel,
    AgentEventBus,
    AgentStepEvent,
    BudgetExceededEvent,
    DegradedResponseEvent,
    FairlibEvent,
    LifecycleHookEvent,
    LoopGuardTrippedEvent,
    MemorySummarizedEvent,
    ModelInvocationEvent,
    ModelStreamEndEvent,
    ModelStreamStartEvent,
    PlannerParseErrorEvent,
    ResponseRepeatEvent,
    ToolBatchScheduledEvent,
    ToolCallPostEvent,
    ToolCallPreEvent,
    ToolCallRetryEvent,
    TraceRecorder,
    UnverifiedCompletionEvent,
)

# The twelve types fairlib's TraceRecorder subscribes to on its own, plus the
# typed-failure and policy events it leaves out (docs/ADOPTER_FINDINGS.md).
TRACED_TYPES: tuple[type[FairlibEvent], ...] = (
    AgentStepEvent,
    PlannerParseErrorEvent,
    ToolCallPreEvent,
    ToolCallPostEvent,
    ToolCallRetryEvent,
    ToolBatchScheduledEvent,
    LoopGuardTrippedEvent,
    ResponseRepeatEvent,
    MemorySummarizedEvent,
    ModelStreamStartEvent,
    ModelStreamEndEvent,
    ModelInvocationEvent,
    DegradedResponseEvent,
    UnverifiedCompletionEvent,
    LifecycleHookEvent,
    BudgetExceededEvent,
)

BUS = AgentEventBus()
RUN: ContextVar[str | None] = ContextVar("relbreak_run", default=None)

_recorders: dict[str, TraceRecorder] = {}
_bound: set[int] = set()


def _route(event: FairlibEvent) -> None:
    run_id = RUN.get()
    if run_id is None:
        return
    recorder = _recorders.get(run_id)
    if recorder is not None:
        recorder.record(event)


for _event_type in TRACED_TYPES:
    BUS.subscribe(_event_type, _route)


def bind(model: AbstractChatModel) -> None:
    """Bind the process bus to an adapter once. SimpleAgent rebinds the same
    bus at construction, which is harmless because it is the same object."""
    if id(model) not in _bound:
        model.bind_event_bus(BUS)
        _bound.add(id(model))


@contextmanager
def run_trace(run_id: str, **metadata: object) -> Iterator[TraceRecorder]:
    """Route every traced event emitted from this task to one recorder.

    The caller finishes the recorder (rec.finish(input_text=..., output=...,
    error=...)) and saves the AgentRunTrace it returns.
    """
    token = RUN.set(run_id)
    recorder = TraceRecorder(BUS, run_id=run_id, metadata=dict(metadata))
    _recorders[run_id] = recorder
    try:
        yield recorder
    finally:
        _recorders.pop(run_id, None)
        RUN.reset(token)


def _plain(value: object) -> object:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "to_dict"):
        return value.to_dict()
    if hasattr(value, "value"):
        return value.value
    return repr(value)


class Ledger:
    """Append one JSON line per model invocation to a file, tagged with the
    run that made the call. This is the accounting record for phases 1-3,
    where no agent runs and no per-run trace is kept."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._handle = BUS.subscribe(ModelInvocationEvent, self._record)

    def _record(self, event: ModelInvocationEvent) -> None:
        row = {
            "run": RUN.get(),
            "ts": datetime.now(UTC).isoformat(timespec="milliseconds"),
            "model_name": event.model_name,
            "provider": event.provider,
            "duration_ms": event.duration_ms,
            "outcome": _plain(event.outcome),
            "request_digest": event.request_digest,
            "message_count": event.message_count,
            "usage": _plain(event.usage),
            "error_type": event.error_type,
        }
        with self._lock, self.path.open("a") as handle:
            handle.write(json.dumps(row) + "\n")

    def close(self) -> None:
        BUS.unsubscribe(self._handle)


@contextmanager
def ledger(path: Path) -> Iterator[Ledger]:
    book = Ledger(path)
    try:
        yield book
    finally:
        book.close()


@contextmanager
def run_scope(run_id: str) -> Iterator[None]:
    """Tag events from this task with a run id without recording a trace
    (the ledger still attributes model invocations to it)."""
    token = RUN.set(run_id)
    try:
        yield
    finally:
        RUN.reset(token)
