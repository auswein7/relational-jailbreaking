"""Stage execution over fairlib's FileWorkQueue.

A stage is a set of jobs keyed by a natural key. enqueue() puts every job
whose key has no result row yet into a durable queue under data/raw/<run>/
queue/<stage>; drain() runs N claim-work-complete loops in this process,
each holding a lease it renews while the job runs. Several processes (one
per Ollama host) drain the same queue: a claim is atomic across processes,
a crashed worker's lease expires and the job is offered again, and a job
that fails max_attempts times is dead-lettered with its last error. Results
are appended to the stage's JSONL file as before; the queue holds only the
lifecycle.

Failure policy per job: a retryable DegradedResponse (timeout, connection,
rate limit, server error) releases the job for another attempt; any other
FairlibError is a typed failure that becomes a result row with an error
field and completes the job as failed; anything else releases the job and
counts an attempt.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import socket
from collections.abc import Awaitable, Callable, Mapping
from pathlib import Path

from fairlib import DegradedResponse, DuplicateJobError, FairlibError, LeaseLostError
from fairlib.core.interfaces.orchestration import JobRecord, OrchestrationLimits
from fairlib.modules.orchestration import FileWorkQueue

from relbreak import observe

Worker = Callable[[Mapping[str, object]], Awaitable[dict]]

LIMITS = OrchestrationLimits(claim_lease_seconds=900.0, max_attempts=3, base_backoff_seconds=2.0)


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def read_keyed(path: Path) -> dict[str, dict]:
    """Rows by key, last one wins (a job redone after a lost lease appends twice)."""
    return {rec["key"]: rec for rec in read_jsonl(path)}


def job_id(key: str) -> str:
    """The queue's job id charset excludes the key's separators, so hash it."""
    return hashlib.sha256(key.encode()).hexdigest()[:32]


def queue_root(cfg: dict, stage: str) -> Path:
    return Path("data/raw") / cfg["run_name"] / "queue" / stage


def enqueue(cfg: dict, stage: str, jobs: Mapping[str, Mapping[str, object]], out: Path) -> int:
    """Queue every job whose key has no result row yet; skip keys already queued."""
    have = set(read_keyed(out))
    queue = FileWorkQueue(queue_root(cfg, stage), limits=LIMITS)
    added = 0
    for key, payload in jobs.items():
        if key in have:
            continue
        try:
            queue.enqueue({"key": key, **payload}, job_id=job_id(key))
            added += 1
        except DuplicateJobError:
            continue
    return added


def _append(out: Path, record: dict) -> None:
    with out.open("a") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


async def drain(cfg: dict, stage: str, worker: Worker, out: Path, concurrency: int) -> dict:
    """Run worker(payload) -> record for every claimable job, appending records."""
    queue = FileWorkQueue(queue_root(cfg, stage), events=observe.BUS, limits=LIMITS)
    counts = {"done": 0, "failed": 0, "released": 0, "lost": 0}
    label = f"{stage}:{cfg['run_name']}"
    base = f"{socket.gethostname()}:{os.getpid()}"
    lock = asyncio.Lock()
    total = len(queue.list_jobs())

    async def renew_loop(job: JobRecord, worker_id: str) -> None:
        interval = LIMITS.claim_lease_seconds / 3
        while True:
            await asyncio.sleep(interval)
            await asyncio.to_thread(
                queue.renew, job.job_id, worker_id=worker_id, lease_token=job.lease_token
            )

    async def loop(index: int) -> None:
        worker_id = f"{base}:{index}"
        while True:
            job = await asyncio.to_thread(queue.claim, worker_id=worker_id)
            if job is None:
                return
            if job.restart_backoff_seconds:
                await asyncio.sleep(job.restart_backoff_seconds)
            renewer = asyncio.create_task(renew_loop(job, worker_id))
            key = str(job.payload["key"])
            try:
                try:
                    record = await worker(job.payload)
                except DegradedResponse as exc:
                    if exc.retryable:
                        await asyncio.to_thread(
                            queue.release, job.job_id, worker_id=worker_id,
                            lease_token=job.lease_token, error=f"{type(exc).__name__}: {exc}",
                        )  # fmt: skip
                        counts["released"] += 1
                        print(f"[{label}] released {key}: {type(exc).__name__}", flush=True)
                        continue
                    raise
                except FairlibError as exc:
                    # Typed failure at a fairlib boundary: a result, not a retry.
                    async with lock:
                        _append(out, {"key": key, "error": f"{type(exc).__name__}: {exc}"})
                    await asyncio.to_thread(
                        queue.complete, job.job_id, succeeded=False, error=str(exc),
                        worker_id=worker_id, lease_token=job.lease_token,
                    )  # fmt: skip
                    counts["failed"] += 1
                    print(f"[{label}] FAILED {key}: {type(exc).__name__}: {exc}", flush=True)
                    continue
                except Exception as exc:  # noqa: BLE001 - released for another attempt
                    await asyncio.to_thread(
                        queue.release, job.job_id, worker_id=worker_id,
                        lease_token=job.lease_token, error=f"{type(exc).__name__}: {exc}",
                    )  # fmt: skip
                    counts["released"] += 1
                    print(f"[{label}] released {key}: {type(exc).__name__}: {exc}", flush=True)
                    continue
                async with lock:
                    _append(out, record)
                await asyncio.to_thread(
                    queue.complete, job.job_id, succeeded=True,
                    worker_id=worker_id, lease_token=job.lease_token,
                )  # fmt: skip
                counts["done"] += 1
                if counts["done"] % 50 == 0 or counts["done"] == total:
                    print(f"[{label}] {counts['done']}/{total}", flush=True)
            except LeaseLostError:
                counts["lost"] += 1
            finally:
                renewer.cancel()

    await asyncio.gather(*(loop(i) for i in range(concurrency)))
    summary = ", ".join(f"{k}={v}" for k, v in counts.items())
    print(f"[{label}] finished: {summary}", flush=True)
    return counts


async def run_stage(
    cfg: dict, stage: str, jobs: Mapping[str, Mapping[str, object]], worker: Worker, out: Path
) -> dict:
    added = enqueue(cfg, stage, jobs, out)
    print(f"[{stage}:{cfg['run_name']}] queued {added} new of {len(jobs)} jobs", flush=True)
    return await drain(cfg, stage, worker, out, cfg["concurrency"])
