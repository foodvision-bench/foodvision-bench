"""Example: subclass FoodRecognitionSystem with a trivial custom model.

Replace ``MyCustomModel.identify`` / ``estimate_portion`` with calls into
your own model. Run:

    python examples/add_custom_system.py
"""
from __future__ import annotations

from typing import Any

from foodvision_bench.core import BenchmarkRunner
from foodvision_bench.systems.base import FoodRecognitionSystem


class MyCustomModel(FoodRecognitionSystem):
    """A trivial model that always predicts "pizza" at 300 kcal.

    Useful for a sanity check: BenchmarkRunner should report roughly the
    MAPE of the always-pizza-300-kcal baseline on your dataset, and a
    top-1 accuracy equal to the fraction of samples that happen to be
    pizza.
    """

    name = "always-pizza-300"
    version = "0.1.0"
    kind = "open-source"

    def identify(self, image: Any) -> dict[str, Any]:  # noqa: ARG002
        return {"label": "pizza", "confidence": 1.0}

    def estimate_portion(self, image: Any) -> dict[str, Any]:  # noqa: ARG002
        return {"label": "pizza", "kcal": 300.0, "grams": 150.0}


def main() -> int:
    # A tiny in-memory dataset for demonstration. In real use, load
    # images with ``load_images_from_dir`` or ``load_hf_food101``.
    samples = [
        ("img-1", {"label": "pizza", "kcal": 290.0}),
        ("img-2", {"label": "pizza", "kcal": 310.0}),
        ("img-3", {"label": "ramen", "kcal": 420.0}),
        ("img-4", {"label": "sushi", "kcal": 180.0}),
    ]

    runner = BenchmarkRunner(MyCustomModel(), test_set_name="mini-4")
    result = runner.run(samples)

    print("system:          ", result.system_name)
    print("n:               ", result.n)
    print(f"top-1 accuracy:   {result.top_1:.3f}")
    print(f"MAPE (kcal):      {result.mape_kcal * 100:.1f}%")
    print("per-category:    ", result.per_category)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
