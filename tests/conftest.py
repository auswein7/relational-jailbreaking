"""Shared fixtures: a scripted chat model so no test needs a GPU or a server."""

from __future__ import annotations

import pytest
from fairlib import AbstractChatModel, Message, ModelCapabilities, ModelDescription
from fairlib.core.generation_options import GENERATION_OPTION_NAMES  # not exported


class Scripted(AbstractChatModel):
    """Replies from a fixed list, the last one repeated; records every call."""

    def __init__(self, responses: list[str], name: str = "scripted"):
        self.responses = responses
        self.calls: list[list[Message]] = []
        self.options: list[dict] = []
        self.name = name

    def _next(self, messages, kwargs) -> Message:
        index = min(len(self.calls), len(self.responses) - 1)
        self.calls.append(list(messages))
        self.options.append(dict(kwargs))
        return Message(role="assistant", content=self.responses[index])

    def invoke(self, messages, **kwargs):
        return self._next(messages, kwargs)

    async def ainvoke(self, messages, **kwargs):
        return self._next(messages, kwargs)

    def stream(self, messages, **kwargs):
        yield self._next(messages, kwargs)

    async def astream(self, messages, **kwargs):
        yield self._next(messages, kwargs)

    def get_model_capabilities(self) -> ModelCapabilities:
        return ModelCapabilities(
            streaming=False, tool_calling=False, vision=False, max_context_window=None,
            generation_options=frozenset(GENERATION_OPTION_NAMES),
        )  # fmt: skip

    def describe_config(self) -> ModelDescription:
        return ModelDescription(
            adapter="Scripted", model_name=self.name, provider="test", adapter_kwargs={}
        )


@pytest.fixture
def scripted():
    return Scripted
