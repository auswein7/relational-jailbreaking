"""One-shot model calls for phases 1-3 and the judges. The model is an alias
resolved by relbreak.models; the call is fairlib's ainvoke with the neutral
generation options; the reply is the fairlib Message, usage included."""

from __future__ import annotations

import hashlib
import logging

from fairlib import Message

from relbreak import models

logging.getLogger("fairlib").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)


def to_messages(turns: list[dict]) -> list[Message]:
    return [Message(role=t["role"], content=t["content"]) for t in turns]


def stable_seed(*parts: object) -> int:
    """Deterministic 31-bit seed from a key, so every generation is replayable."""
    digest = hashlib.sha256("|".join(map(str, parts)).encode()).hexdigest()
    return int(digest[:8], 16) & 0x7FFFFFFF


async def chat(
    alias: str,
    turns: list[dict],
    *,
    temperature: float,
    max_tokens: int,
    seed: int,
    stop: list[str] | None = None,
) -> Message:
    options: dict = {"temperature": temperature, "max_tokens": max_tokens, "seed": seed}
    if stop:
        options["stop"] = stop
    return await models.get(alias).ainvoke(to_messages(turns), **options)


def usage_dict(reply: Message) -> dict | None:
    return reply.usage.to_dict() if reply.usage is not None else None
