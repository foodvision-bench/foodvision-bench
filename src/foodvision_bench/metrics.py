"""Evaluation metrics for food-recognition benchmarks.

All metrics take plain lists or numpy arrays so they can be used without
pulling in torch or a full training harness.
"""
from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable, Sequence
from typing import Any

import numpy as np


def _as_array(x: Iterable[float]) -> np.ndarray:
    arr = np.asarray(list(x), dtype=np.float64)
    if arr.ndim != 1:
        raise ValueError(f"expected 1-D sequence, got shape {arr.shape}")
    return arr


def mape(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    """Mean Absolute Percent Error.

    Returned as a fraction (e.g. 0.084 for 8.4%), not as a percentage.

    Raises
    ------
    ValueError
        If the inputs have different lengths, are empty, or contain a zero
        in ``y_true`` (which would make percent error undefined).
    """
    yt = _as_array(y_true)
    yp = _as_array(y_pred)
    if yt.shape != yp.shape:
        raise ValueError(f"shape mismatch: y_true {yt.shape} vs y_pred {yp.shape}")
    if yt.size == 0:
        raise ValueError("cannot compute MAPE on empty input")
    if np.any(yt == 0):
        raise ValueError("y_true contains zero; MAPE is undefined")
    return float(np.mean(np.abs((yt - yp) / yt)))


def top_1_accuracy(
    y_true: Sequence[Any],
    y_pred: Sequence[Any],
) -> float:
    """Top-1 classification accuracy as a fraction in [0, 1]."""
    if len(y_true) != len(y_pred):
        raise ValueError(
            f"length mismatch: y_true={len(y_true)} y_pred={len(y_pred)}"
        )
    if len(y_true) == 0:
        raise ValueError("cannot compute accuracy on empty input")
    correct = sum(1 for a, b in zip(y_true, y_pred, strict=True) if a == b)
    return correct / len(y_true)


def per_category_breakdown(
    y_true_labels: Sequence[Any],
    y_true_kcal: Sequence[float],
    y_pred_kcal: Sequence[float],
) -> dict[str, dict[str, float]]:
    """Group MAPE and sample count by ground-truth category label.

    Returns a mapping ``{category: {"mape": float, "n": int}}`` so callers
    can sort / threshold / render a table.
    """
    if not (len(y_true_labels) == len(y_true_kcal) == len(y_pred_kcal)):
        raise ValueError("all three input sequences must be the same length")
    if len(y_true_labels) == 0:
        return {}

    buckets: dict[Any, list[tuple[float, float]]] = defaultdict(list)
    for label, t, p in zip(y_true_labels, y_true_kcal, y_pred_kcal, strict=True):
        buckets[label].append((float(t), float(p)))

    out: dict[str, dict[str, float]] = {}
    for label, pairs in buckets.items():
        trues = [t for t, _ in pairs]
        preds = [p for _, p in pairs]
        try:
            cat_mape = mape(trues, preds)
        except ValueError:
            # e.g. zero in trues for that category
            cat_mape = float("nan")
        out[str(label)] = {"mape": cat_mape, "n": len(pairs)}
    return out
