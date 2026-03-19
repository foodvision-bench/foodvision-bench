"""Tests for the metrics module."""
from __future__ import annotations

import math

import pytest

from foodvision_bench.metrics import mape, per_category_breakdown, top_1_accuracy


def test_mape_perfect_prediction_is_zero():
    assert mape([100.0, 200.0, 300.0], [100.0, 200.0, 300.0]) == 0.0


def test_mape_known_value():
    # MAPE = mean(|(100-110)/100|, |(200-180)/200|) = mean(0.1, 0.1) = 0.1
    assert math.isclose(mape([100.0, 200.0], [110.0, 180.0]), 0.10, abs_tol=1e-9)


def test_mape_length_mismatch_raises():
    with pytest.raises(ValueError):
        mape([1.0, 2.0], [1.0, 2.0, 3.0])


def test_mape_empty_raises():
    with pytest.raises(ValueError):
        mape([], [])


def test_mape_zero_in_truth_raises():
    # zero in y_true makes % error undefined
    with pytest.raises(ValueError):
        mape([0.0, 100.0], [10.0, 100.0])


def test_top_1_accuracy_all_correct():
    assert top_1_accuracy(["pizza", "ramen"], ["pizza", "ramen"]) == 1.0


def test_top_1_accuracy_half_correct():
    assert top_1_accuracy(
        ["pizza", "ramen", "sushi", "tacos"],
        ["pizza", "sushi", "sushi", "pizza"],
    ) == 0.5


def test_top_1_accuracy_length_mismatch_raises():
    with pytest.raises(ValueError):
        top_1_accuracy(["a", "b"], ["a"])


def test_top_1_accuracy_empty_raises():
    with pytest.raises(ValueError):
        top_1_accuracy([], [])


def test_per_category_breakdown_groups_and_counts():
    labels = ["pizza", "pizza", "ramen"]
    true_kcal = [300.0, 310.0, 400.0]
    pred_kcal = [330.0, 290.0, 450.0]
    out = per_category_breakdown(labels, true_kcal, pred_kcal)
    assert set(out) == {"pizza", "ramen"}
    assert out["pizza"]["n"] == 2
    assert out["ramen"]["n"] == 1
    # pizza: mean(|30/300|, |20/310|)
    assert out["pizza"]["mape"] == pytest.approx(
        (abs((300.0 - 330.0) / 300.0) + abs((310.0 - 290.0) / 310.0)) / 2,
        rel=1e-9,
    )
    # ramen: |50/400| = 0.125
    assert out["ramen"]["mape"] == pytest.approx(0.125, rel=1e-9)


def test_per_category_breakdown_empty_returns_empty():
    assert per_category_breakdown([], [], []) == {}


def test_per_category_breakdown_length_mismatch_raises():
    with pytest.raises(ValueError):
        per_category_breakdown(["a"], [1.0, 2.0], [1.0, 2.0])
