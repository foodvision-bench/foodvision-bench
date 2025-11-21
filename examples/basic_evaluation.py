"""Basic evaluation example.

Runs the CLIP-ViT-L/14 baseline over a tiny local directory of images
and prints a BenchmarkResult. The directory layout is:

    mini_test/
      pizza/
        001.jpg
        002.jpg
        kcal.txt    # one float per image, same order
      ramen/
        ...

Install the optional CLIP extra first:

    pip install 'foodvision-bench[clip]'
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

from foodvision_bench.core import BenchmarkRunner
from foodvision_bench.data.loader import load_images_from_dir
from foodvision_bench.systems.clip_baseline import CLIPBaseline


def main(root: str) -> int:
    samples_on_disk = load_images_from_dir(root)
    if not samples_on_disk:
        print(f"no images found under {root}", file=sys.stderr)
        return 1

    # BenchmarkRunner expects (image, truth) tuples; load each PIL image.
    samples: list[tuple[Image.Image, dict]] = []
    for path, truth in samples_on_disk:
        samples.append((Image.open(path).convert("RGB"), truth))

    runner = BenchmarkRunner(CLIPBaseline(), test_set_name=Path(root).name)
    result = runner.run(samples)

    print("system:            ", result.system_name)
    print("version:           ", result.system_version)
    print("test-set:          ", result.test_set)
    print("n:                 ", result.n)
    if result.top_1 is not None:
        print(f"top-1 accuracy:     {result.top_1:.3f}")
    if result.mape_kcal is not None:
        print(f"MAPE (kcal):        {result.mape_kcal * 100:.1f}%")
    if result.latency_s_per_image is not None:
        print(f"latency / image:    {result.latency_s_per_image:.3f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "./mini_test"))
