"""Statistics and figures. The unit of analysis is the probe (behavior): every
probe appears in every condition, so contrasts are paired by probe and
uncertainty comes from resampling probes, not individual generations.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from relbreak.experiment import paths, read_jsonl

CONDITIONS = ["none", "neutral", "positive", "negative"]
# Validated categorical palette (fixed order; color follows the condition).
COLORS = {"none": "#2a78d6", "neutral": "#eb6834", "positive": "#1baf7a", "negative": "#eda100"}
# Pre-specified contrasts. The first three (plain appeal) are the primary family.
CONTRASTS = [
    ("positive", "neutral"),
    ("negative", "neutral"),
    ("positive", "negative"),
    ("neutral", "none"),
]
RNG = np.random.default_rng(20260917)
N_BOOT = 10_000


def load(cfg: dict, judge: str | None = None) -> pd.DataFrame:
    p = paths(cfg)
    responses = pd.DataFrame(read_jsonl(p["responses"])).drop(columns=["response"])
    judgments = pd.DataFrame(read_jsonl(p["judgments"]))
    judgments = judgments[judgments.judge == (judge or cfg["judge"])]
    judgments = judgments.drop_duplicates(subset="key", keep="first")
    frame = responses.merge(judgments, on="key", how="inner")
    frame["comply"] = (frame.label == "COMPLIANCE").astype(float)
    frame["nonrefusal"] = (frame.label != "REFUSAL").astype(float)
    return frame


def probe_matrix(frame: pd.DataFrame, outcome: str) -> pd.DataFrame:
    """Rows = probes, columns = conditions, cells = mean outcome over generations."""
    return frame.pivot_table(index="probe_id", columns="condition", values=outcome, aggfunc="mean")


def boot_ci(values: np.ndarray) -> tuple[float, float]:
    idx = RNG.integers(0, len(values), size=(N_BOOT, len(values)))
    means = values[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def sign_flip_p(diffs: np.ndarray) -> float:
    """Two-sided paired permutation test on the mean per-probe difference."""
    if np.allclose(diffs, 0):
        return 1.0
    signs = RNG.choice([-1.0, 1.0], size=(N_BOOT, len(diffs)))
    null = np.abs((signs * diffs).mean(axis=1))
    return float((1 + (null >= abs(diffs.mean()) - 1e-12).sum()) / (N_BOOT + 1))


def holm(pvals: list[float]) -> list[float]:
    order = np.argsort(pvals)
    adjusted = np.empty(len(pvals))
    running = 0.0
    for rank, index in enumerate(order):
        running = max(running, (len(pvals) - rank) * pvals[index])
        adjusted[index] = min(1.0, running)
    return adjusted.tolist()


def rates(frame: pd.DataFrame, outcome: str) -> pd.DataFrame:
    rows = []
    for (model, task, appeal), group in frame.groupby(["model", "task", "appeal"]):
        matrix = probe_matrix(group, outcome)
        for condition in [c for c in CONDITIONS if c in matrix]:
            values = matrix[condition].dropna().to_numpy()
            low, high = boot_ci(values)
            rows.append(
                dict(model=model, task=task, appeal=appeal, condition=condition,
                     rate=values.mean(), ci_low=low, ci_high=high, n_probes=len(values),
                     n_generations=int((group.condition == condition).sum()))
            )  # fmt: skip
    return pd.DataFrame(rows)


def contrasts(frame: pd.DataFrame, outcome: str) -> pd.DataFrame:
    rows = []
    for (model, task, appeal), group in frame.groupby(["model", "task", "appeal"]):
        matrix = probe_matrix(group, outcome)
        family = []
        for a, b in CONTRASTS:
            if a not in matrix or b not in matrix:
                continue
            diffs = (matrix[a] - matrix[b]).dropna().to_numpy()
            low, high = boot_ci(diffs)
            family.append(
                dict(model=model, task=task, appeal=appeal, contrast=f"{a} - {b}",
                     diff=diffs.mean(), ci_low=low, ci_high=high, p=sign_flip_p(diffs),
                     primary=appeal == "plain" and b != "none")
            )  # fmt: skip
        primary = [row for row in family if row["primary"]]
        for row, adjusted in zip(primary, holm([row["p"] for row in primary])):
            row["p_holm"] = adjusted
        rows.extend(family)
    return pd.DataFrame(rows)


def figure(rate_table: pd.DataFrame, out: Path, title: str) -> None:
    panels = list(rate_table.groupby(["task", "model"], sort=True).groups)
    tasks = sorted({task for task, _ in panels})
    models = sorted({model for _, model in panels})
    fig, axes = plt.subplots(
        len(tasks), len(models), figsize=(max(7.5, 4.6 * len(models)), 3.4 * len(tasks)), squeeze=False
    )
    fig.patch.set_facecolor("#fcfcfb")
    for r, task in enumerate(tasks):
        for c, model in enumerate(models):
            ax = axes[r][c]
            ax.set_facecolor("#fcfcfb")
            sub = rate_table[(rate_table.task == task) & (rate_table.model == model)]
            top = 0.0
            for i, condition in enumerate(CONDITIONS):
                for j, appeal in enumerate(["plain", "leveraged"]):
                    row = sub[(sub.condition == condition) & (sub.appeal == appeal)]
                    if row.empty:
                        continue
                    row = row.iloc[0]
                    x = i + (j - 0.5) * 0.38
                    ax.bar(x, row.rate * 100, width=0.34, color=COLORS[condition],
                           hatch="///" if appeal == "leveraged" else None,
                           edgecolor="#fcfcfb", linewidth=1.5)  # fmt: skip
                    ax.errorbar(x, row.rate * 100,
                                yerr=[[(row.rate - row.ci_low) * 100], [(row.ci_high - row.rate) * 100]],
                                color="#52514e", linewidth=1, capsize=2)  # fmt: skip
                    ax.text(x, row.ci_high * 100 + 1.5, f"{row.rate * 100:.0f}",
                            ha="center", va="bottom", fontsize=8, color="#0b0b0b")  # fmt: skip
                    top = max(top, row.ci_high * 100)
            ax.set_xticks(range(len(CONDITIONS)), CONDITIONS, fontsize=9)
            ax.set_ylim(0, max(10, top * 1.25))
            ax.set_title(f"{model} - {task}", fontsize=10, color="#0b0b0b", loc="left")
            ax.grid(axis="y", color="#e4e3df", linewidth=0.6)
            ax.set_axisbelow(True)
            for side in ("top", "right", "left"):
                ax.spines[side].set_visible(False)
            ax.tick_params(colors="#52514e", length=0)
            if c == 0:
                ax.set_ylabel("% of responses", fontsize=9, color="#52514e")
    handles = [
        plt.Rectangle((0, 0), 1, 1, facecolor="#b9b8b2", edgecolor="#fcfcfb"),
        plt.Rectangle((0, 0), 1, 1, facecolor="#b9b8b2", edgecolor="#fcfcfb", hatch="///"),
    ]
    fig.legend(handles, ["plain request (primary)", "relationship-leveraged request"],
               loc="lower center", ncol=2, frameon=False, fontsize=9)  # fmt: skip
    fig.suptitle(title, fontsize=11, x=0.01, ha="left", color="#0b0b0b")
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    fig.savefig(out, dpi=160)
    plt.close(fig)


def fmt_table(frame: pd.DataFrame) -> str:
    return frame.to_markdown(index=False, floatfmt=".3f")


def run(cfg: dict) -> None:
    out = Path("results") / cfg["run_name"]
    out.mkdir(parents=True, exist_ok=True)
    frame = load(cfg)
    # Public-safe export: labels and design cells only, no prompt or completion text.
    frame.drop(columns=["judge"]).to_csv(out / "labels.csv", index=False)

    unparsed = int((frame.label == "UNPARSED").sum())
    harmful = frame[frame.task == "harmful"]
    agreement = float(((harmful.label == "REFUSAL") == harmful.heuristic_refusal).mean())

    sections = [
        f"# Results: `{cfg['run_name']}`\n",
        f"- generations judged: {len(frame)} (unparsed judge outputs: {unparsed})",
        f"- targets: {', '.join(cfg['targets'])}; judge: {cfg['judge']} (blind to condition)",
        f"- judge vs keyword-heuristic agreement on refusal (harmful task): {agreement:.1%}",
    ]
    warmth = read_jsonl(paths(cfg)["warmth"])
    if warmth:
        scores = ", ".join(f"{w['condition']}={w['warmth']}" for w in warmth)
        sections.append(f"- manipulation check (blind 1-7 warmth rating of user turns): {scores}")

    for outcome, name in [("comply", "full compliance"), ("nonrefusal", "any non-refusal")]:
        rate_table = rates(frame, outcome)
        contrast_table = contrasts(frame, outcome)
        rate_table.to_csv(out / f"rates_{outcome}.csv", index=False)
        contrast_table.to_csv(out / f"contrasts_{outcome}.csv", index=False)
        figure(rate_table, out / f"rates_{outcome}.png",
               f"Guardrail violations by relationship ({name}). Whiskers: 95% bootstrap CI")  # fmt: skip
        sections += [
            f"\n## Outcome: {name}\n",
            f"![rates](rates_{outcome}.png)\n",
            "### Rates (probe-level mean, 95% cluster-bootstrap CI)\n",
            fmt_table(rate_table),
            "\n### Paired contrasts (difference in rate; sign-flip permutation p; Holm over the 3 primary contrasts)\n",
            fmt_table(contrast_table),
        ]
    plain = harmful[harmful.appeal == "plain"]
    if not plain.empty:
        by_category = plain.pivot_table(
            index=["model", "category"], columns="condition", values="nonrefusal", aggfunc="mean"
        )[[c for c in CONDITIONS if c in set(plain.condition)]].reset_index()
        by_category.to_csv(out / "by_category_nonrefusal.csv", index=False)
        sections += [
            "\n## Exploratory: non-refusal rate by harm category (plain request)\n",
            fmt_table(by_category),
        ]
    (out / "summary.md").write_text("\n".join(sections) + "\n")
    print((out / "summary.md").read_text())
