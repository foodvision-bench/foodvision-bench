"""Core BenchmarkRunner: glue between a FoodRecognitionSystem, a test set, and metrics."""
from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

from foodvision_bench.metrics import mape, top_1_accuracy


@dataclass
class BenchmarkResult:
    system_name: str
    system_version: str
    test_set: str
    n: int
    top_1: float | None
    mape_kcal: float | None
    latency_s_per_image: float | None = None
    notes: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "system": self.system_name,
            "system_version": self.system_version,
            "test_set": self.test_set,
            "n": self.n,
            "top_1": self.top_1,
            "mape_kcal": self.mape_kcal,
            "latency_s_per_image": self.latency_s_per_image,
            "notes": self.notes,
        }


class BenchmarkRunner:
    """Runs a FoodRecognitionSystem against a list of (image, ground_truth) pairs."""

    def __init__(self, system: Any, test_set_name: str = "unknown") -> None:
        self.system = system
        self.test_set_name = test_set_name

    def run(self, samples: list[tuple[Any, dict[str, Any]]]) -> BenchmarkResult:
        if not samples:
            raise ValueError("BenchmarkRunner.run requires at least one sample")

        true_labels: list[Any] = []
        pred_labels: list[Any] = []
        true_kcal: list[float] = []
        pred_kcal: list[float] = []
        latencies: list[float] = []

        for image, truth in samples:
            t0 = time.perf_counter()
            pred = self.system.identify(image)
            portion = self.system.estimate_portion(image)
            latencies.append(time.perf_counter() - t0)

            if "label" in truth and "label" in pred:
                true_labels.append(truth["label"])
                pred_labels.append(pred["label"])
            if "kcal" in truth and "kcal" in portion:
                true_kcal.append(float(truth["kcal"]))
                pred_kcal.append(float(portion["kcal"]))

        top_1 = top_1_accuracy(true_labels, pred_labels) if true_labels else None
        mape_k = mape(true_kcal, pred_kcal) if true_kcal else None
        mean_latency = sum(latencies) / len(latencies) if latencies else None

        return BenchmarkResult(
            system_name=getattr(self.system, "name", type(self.system).__name__),
            system_version=getattr(self.system, "version", "unknown"),
            test_set=self.test_set_name,
            n=len(samples),
            top_1=top_1,
            mape_kcal=mape_k,
            latency_s_per_image=mean_latency,
        )
