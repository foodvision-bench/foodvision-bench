"""Tests for the system base class and a mocked CLIP baseline."""
from __future__ import annotations

from unittest.mock import patch

import pytest

from foodvision_bench.core import BenchmarkRunner
from foodvision_bench.systems import REGISTRY, load_system
from foodvision_bench.systems.base import FoodRecognitionSystem
from foodvision_bench.systems.clip_baseline import CLIPBaseline


class _DummySystem(FoodRecognitionSystem):
    name = "dummy"
    version = "0.0.1"
    kind = "open-source"

    def identify(self, image):  # noqa: ARG002
        return {"label": "pizza", "confidence": 0.9}

    def estimate_portion(self, image):  # noqa: ARG002
        return {"label": "pizza", "kcal": 300.0, "grams": 150.0}


def test_base_requires_subclass():
    with pytest.raises(TypeError):
        FoodRecognitionSystem()  # type: ignore[abstract]


def test_dummy_system_metadata():
    s = _DummySystem()
    meta = s.metadata()
    assert meta["name"] == "dummy"
    assert meta["kind"] == "open-source"


def test_runner_with_dummy_system_computes_metrics():
    system = _DummySystem()
    samples = [
        ("image-a", {"label": "pizza", "kcal": 290.0}),
        ("image-b", {"label": "pizza", "kcal": 310.0}),
        ("image-c", {"label": "ramen", "kcal": 400.0}),
    ]
    runner = BenchmarkRunner(system, test_set_name="mini-3")
    result = runner.run(samples)
    assert result.n == 3
    assert result.top_1 == pytest.approx(2 / 3)
    assert result.mape_kcal is not None


def test_runner_empty_raises():
    runner = BenchmarkRunner(_DummySystem(), test_set_name="mini-3")
    with pytest.raises(ValueError):
        runner.run([])


def test_registry_has_clip():
    assert "clip-vit-l" in REGISTRY


def test_load_system_unknown_key():
    with pytest.raises(KeyError):
        load_system("not-a-real-system")


def test_clip_baseline_identify_is_mockable():
    # We don't want to pull real weights in CI. Mock the lazy loader.
    fake_predict = {"label": "pizza", "confidence": 0.72}
    with patch.object(CLIPBaseline, "_ensure_loaded", lambda self: None), \
         patch.object(CLIPBaseline, "identify", return_value=fake_predict):
        sys = CLIPBaseline()
        out = sys.identify("fake-image")
        assert out == fake_predict
