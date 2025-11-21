"""Image loaders.

Two entry points:

- ``load_images_from_dir(root)`` walks a local directory whose layout is
  ``<root>/<label>/<image>.jpg``. Ground-truth kcal, if available, is
  expected in a sibling ``<label>/kcal.txt`` file (single float per line,
  matching image order). Images missing a kcal file are still loaded but
  will have ``kcal=None``.
- ``load_hf_food101`` is a thin wrapper around Hugging Face Datasets'
  Food-101 split. Imported lazily so the rest of the package works without
  the ``datasets`` extra.
"""
from __future__ import annotations

from collections.abc import Iterator
from pathlib import Path
from typing import Any

_IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def load_images_from_dir(root: str | Path) -> list[tuple[Path, dict[str, Any]]]:
    """Walk ``root`` yielding ``(path, truth)`` tuples for evaluation."""
    root = Path(root)
    if not root.is_dir():
        raise FileNotFoundError(f"not a directory: {root}")

    samples: list[tuple[Path, dict[str, Any]]] = []
    for label_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        label = label_dir.name
        kcal_file = label_dir / "kcal.txt"
        kcals: list[float] | None = None
        if kcal_file.exists():
            kcals = [float(line.strip()) for line in kcal_file.read_text().splitlines() if line.strip()]
        images = sorted(
            p for p in label_dir.iterdir() if p.suffix.lower() in _IMAGE_EXTS
        )
        for i, img_path in enumerate(images):
            truth: dict[str, Any] = {"label": label}
            if kcals is not None and i < len(kcals):
                truth["kcal"] = kcals[i]
            samples.append((img_path, truth))
    return samples


def load_hf_food101(split: str = "test[:500]") -> Iterator[tuple[Any, dict[str, Any]]]:
    """Stream (image, truth) pairs from the Hugging Face Food-101 dataset.

    The ``datasets`` package is imported lazily.
    """
    try:
        from datasets import load_dataset  # type: ignore
    except ImportError as exc:
        raise ImportError(
            "load_hf_food101 requires 'datasets'. "
            "Install with: pip install datasets"
        ) from exc

    ds = load_dataset("food101", split=split)
    for row in ds:
        truth = {"label": row["label"]}
        yield row["image"], truth
