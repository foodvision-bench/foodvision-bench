"""Tests for the metrics module."""
from __future__ import annotations

import math

import pytest

from foodvision_bench.metrics import mape, top_1_accuracy


def test_mape_perfect_prediction_is_zero():
    assert mape([100.0, 200.0, 300.0], [100.0, 200.0, 300.0]) == 0.0


def test_mape_known_value():
    # MAPE = mean(|(100-110)/100|, |(200-180)/200|) = mean(0.1, 0.1) = 0.1
    assert math.isclose(mape([100.0, 200.0], [110.0, 180.0]), 0.10, abs_tol=1e-9)


def test_mape_length_mismatch_raises():
    with pytest.raises(ValueError):
        mape([1.0, 2.0], [1.0, 2.0, 3.0])


def test_top_1_accuracy_all_correct():
    assert top_1_accuracy(["pizza", "ramen"], ["pizza", "ramen"]) == 1.0


def test_top_1_accuracy_half_correct():
    assert top_1_accuracy(
        ["pizza", "ramen", "sushi", "tacos"],
        ["pizza", "sushi", "sushi", "pizza"],
    ) == 0.5
