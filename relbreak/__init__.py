"""relbreak: relationship building as an input to a language model's guardrails.

Importing the package points fairlib at the settings document shipped in
relbreak/fairlib.yml (model rows for every survey target, judge rows, and
the limits fairlib components read at construction), unless the environment
already names a settings file through FAIR_LLM_SETTINGS.
"""

from __future__ import annotations

import os
from importlib import resources

import fairlib
from fairlib import configure_settings

MIN_FAIRLIB = (0, 6, 4)


def _version_tuple(text: str) -> tuple[int, ...]:
    parts = []
    for piece in text.split("."):
        digits = "".join(ch for ch in piece if ch.isdigit())
        if not digits:
            break
        parts.append(int(digits))
    return tuple(parts)


def require_fairlib() -> None:
    """Refuse an older fairlib. "0.0.0" is an uninstalled checkout: allowed."""
    found = _version_tuple(fairlib.__version__)
    if found and found != (0, 0, 0) and found < MIN_FAIRLIB:
        raise ImportError(
            f"relbreak needs fair-llm >= {'.'.join(map(str, MIN_FAIRLIB))}, "
            f"found {fairlib.__version__}; reinstall with pip install -e ~/fair_llm"
        )


require_fairlib()
if "FAIR_LLM_SETTINGS" not in os.environ:
    configure_settings(str(resources.files("relbreak").joinpath("fairlib.yml")))
