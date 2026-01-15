"""foodvision-bench: Open reproducible benchmarks for food-image recognition."""

__version__ = "0.1.1"

from foodvision_bench.metrics import mape, top_1_accuracy

__all__ = ["__version__", "mape", "top_1_accuracy"]
