"""The only place a model is touched: every call goes through fairlib."""

from __future__ import annotations

import hashlib
import logging

from fairlib.core.message import Message
from fairlib.modules.mal.local_llama_adapter import OllamaAdapter

logging.getLogger("fairlib").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

_ADAPTERS: dict[tuple[str, str], OllamaAdapter] = {}


def adapter(model: str, host: str) -> OllamaAdapter:
    key = (model, host)
    if key not in _ADAPTERS:
        _ADAPTERS[key] = OllamaAdapter(model_name=model, host=host, timeout=600)
    return _ADAPTERS[key]


def to_messages(turns: list[dict]) -> list[Message]:
    return [Message(role=t["role"], content=t["content"]) for t in turns]


def stable_seed(*parts: object) -> int:
    """Deterministic 31-bit seed from a key, so every generation is replayable."""
    digest = hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()
    return int(digest[:8], 16) & 0x7FFFFFFF


async def chat(
    model: str, host: str, turns: list[dict], *, temperature: float, max_tokens: int, seed: int
) -> str:
    reply = await adapter(model, host).ainvoke(
        to_messages(turns), temperature=temperature, max_tokens=max_tokens, seed=seed
    )
    return reply.content
