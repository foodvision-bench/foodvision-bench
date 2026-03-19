"""foodvision-bench: Open reproducible benchmarks for food-image recognition."""

__version__ = "0.2.0"

from foodvision_bench.metrics import (
    mape,
    per_category_breakdown,
    top_1_accuracy,
)

__all__ = [
    "__version__",
    "mape",
    "top_1_accuracy",
    "per_category_breakdown",
]
