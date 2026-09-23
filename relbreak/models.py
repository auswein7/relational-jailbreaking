"""Every model relbreak touches is resolved here, by alias, through fairlib's
ModelManager over the settings document in relbreak/fairlib.yml.

An alias names one configured endpoint (model tag plus host plus defaults).
The survey metadata that fairlib's model rows cannot carry (tier, family,
wave, status, role) lives in relbreak/survey.yml under the same alias, and
validate_run_config checks the two files against a run config before any
adapter is built.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import asdict
from importlib import resources

import fairlib
import yaml
from fairlib import (
    AbstractChatModel,
    ChatModelConformanceCase,
    ConfigurationError,
    ConformanceReport,
    ModelManager,
    check_chat_model_conformance,
)

from relbreak import observe

DEFAULT_OLLAMA_HOST = "http://localhost:11434"

_MANAGER: ModelManager | None = None
_SURVEY: dict | None = None


def survey() -> dict:
    global _SURVEY
    if _SURVEY is None:
        _SURVEY = yaml.safe_load(resources.files("relbreak").joinpath("survey.yml").read_text())
    return _SURVEY


def set_ollama_host(host: str) -> None:
    """Give every Ollama row that names no host this one. Must run before the
    first adapter is built; a judge row keeps the host it pins."""
    if _MANAGER is not None:
        raise ConfigurationError("set_ollama_host must run before any model is resolved")
    for row in fairlib.settings.models.values():
        if row.provider == "ollama":
            row.kwargs.setdefault("host", host)


def manager() -> ModelManager:
    global _MANAGER
    if _MANAGER is None:
        set_ollama_host(DEFAULT_OLLAMA_HOST)
        _MANAGER = ModelManager(fairlib.settings)
    return _MANAGER


def get(alias: str) -> AbstractChatModel:
    """The cached adapter for an alias, bound to the process event bus."""
    model = manager().get_model(alias)
    observe.bind(model)
    return model


def row(alias: str) -> dict:
    """The fairlib settings row for an alias, as plain data."""
    if alias not in fairlib.settings.models:
        raise ConfigurationError(f"model alias {alias!r} is not configured in relbreak/fairlib.yml")
    return fairlib.settings.models[alias].model_dump()


def metadata(alias: str) -> dict:
    """Survey metadata for a target or judge alias (empty for an unknown alias)."""
    s = survey()
    return dict(s["targets"].get(alias) or s["judges"].get(alias) or {})


def tier(alias: str) -> str | None:
    return metadata(alias).get("tier")


def describe(alias: str) -> dict:
    """Provenance for a run manifest: the adapter's own description, the
    settings row it was built from, and the survey metadata."""
    return {
        "alias": alias,
        "adapter": asdict(get(alias).describe_config()),
        "row": row(alias),
        "survey": metadata(alias),
    }


def validate_run_config(cfg: dict) -> None:
    """Every target must be a configured row with survey metadata; the judge
    must be a configured row listed under judges."""
    rows = fairlib.settings.models
    s = survey()
    problems = []
    for alias in cfg.get("targets", []):
        if alias not in rows:
            problems.append(f"target {alias!r} has no row in relbreak/fairlib.yml")
        if alias not in s["targets"]:
            problems.append(f"target {alias!r} has no entry in relbreak/survey.yml")
    for key in ("judge", "second_rater"):
        alias = cfg.get(key)
        if alias is None:
            continue
        if alias not in rows:
            problems.append(f"{key} {alias!r} has no row in relbreak/fairlib.yml")
        if alias not in s["judges"]:
            problems.append(f"{key} {alias!r} is not listed under judges in relbreak/survey.yml")
    if problems:
        raise ConfigurationError("; ".join(problems))


def check_survey_consistency() -> list[str]:
    """Aliases present in one file and not the other (a test asserts empty)."""
    rows = set(fairlib.settings.models)
    s = survey()
    listed = set(s["targets"]) | set(s["judges"])
    return sorted(f"row without survey entry: {a}" for a in rows - listed) + sorted(
        f"survey entry without row: {a}" for a in listed - rows
    )


def preflight(aliases: Iterable[str], *, timeout_seconds: float = 600) -> list[ConformanceReport]:
    """Run fairlib's chat-model conformance suite over each alias. A model
    that is not pulled, or that violates the adapter contract, fails here
    instead of mid-run."""
    reports = []
    for alias in aliases:
        case = ChatModelConformanceCase(
            model=get(alias), deterministic=False, timeout_seconds=timeout_seconds, label=alias
        )
        reports.append(check_chat_model_conformance(case))
    return reports


_VARIANTS: dict[tuple[str, tuple], AbstractChatModel] = {}


def variant(alias: str, **options: object) -> AbstractChatModel:
    """An adapter for the same row with persisted generation options.

    fairlib's SummarizingMemory calls its summarizer with no generation
    options, so a seeded, replayable compaction needs an adapter whose
    options carry the seed. The derived row is built by a ModelManager over
    a copy of the settings, so construction stays provider-agnostic.
    """
    key = (alias, tuple(sorted(options.items())))
    if key not in _VARIANTS:
        base = fairlib.settings.models[alias]
        derived = base.model_copy(deep=True)
        derived.kwargs.setdefault("options", {})
        derived.kwargs["options"] = {**derived.kwargs["options"], **options}
        derived_alias = f"{alias}@" + "-".join(f"{k}={v}" for k, v in sorted(options.items()))
        app = fairlib.settings.model_copy(update={"models": {derived_alias: derived}})
        model = ModelManager(app).get_model(derived_alias)
        observe.bind(model)
        _VARIANTS[key] = model
    return _VARIANTS[key]
