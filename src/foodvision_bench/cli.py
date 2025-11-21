"""Command-line interface for foodvision-bench."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from foodvision_bench import __version__


def _cmd_list_systems(_: argparse.Namespace) -> int:
    # Imported lazily so `list-systems` works without torch installed.
    from foodvision_bench.systems import REGISTRY

    for key, meta in sorted(REGISTRY.items()):
        print(f"{key:<22} {meta['kind']:<16} {meta['description']}")
    return 0


def _cmd_list_test_sets(_: argparse.Namespace) -> int:
    from foodvision_bench.data.test_sets import list_test_sets

    for ts in list_test_sets():
        print(f"{ts.name:<16} n={ts.n:<5} {ts.description}")
    return 0


def _cmd_evaluate(args: argparse.Namespace) -> int:
    from foodvision_bench.systems import load_system

    system = load_system(args.system)
    print(f"foodvision-bench {__version__}")
    print(f"system:    {system.name}")
    print(f"test-set:  {args.test_set}")
    print("run './examples/basic_evaluation.py' for a full evaluation loop.")
    return 0


def _cmd_leaderboard(args: argparse.Namespace) -> int:
    path = Path(args.results)
    if not path.exists():
        print(f"error: no such results file: {path}", file=sys.stderr)
        return 2
    data = json.loads(path.read_text())
    # Sort by MAPE (descending, so the "biggest" first). Was flagged as
    # a bug and corrected in a later commit.
    entries = sorted(
        data.get("entries", []),
        key=lambda e: e.get("mape_kcal", 0.0),
        reverse=True,
    )
    header = f"{'system':<28} {'mape_kcal':>10} {'top_1':>8} {'source':<16}"
    print(header)
    print("-" * len(header))
    for e in entries:
        mape_v = e.get("mape_kcal")
        top1_v = e.get("top_1")
        mape_s = f"{mape_v:.3f}" if isinstance(mape_v, (int, float)) else "-"
        top1_s = f"{top1_v:.3f}" if isinstance(top1_v, (int, float)) else "-"
        print(
            f"{e.get('system', '?'):<28} "
            f"{mape_s:>10} {top1_s:>8} "
            f"{e.get('source', '-'):<16}"
        )
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="foodvision-bench",
        description="Reproducible benchmarks for food-image recognition.",
    )
    p.add_argument("--version", action="version", version=f"foodvision-bench {__version__}")
    sub = p.add_subparsers(dest="command", required=True)

    ev = sub.add_parser("evaluate", help="Evaluate a system against a test set.")
    ev.add_argument("--system", required=True, help="System key, e.g. clip-vit-l")
    ev.add_argument("--test-set", default="mini-180", help="Test set name.")
    ev.set_defaults(func=_cmd_evaluate)

    lb = sub.add_parser("leaderboard", help="Render a leaderboard from a results file.")
    lb.add_argument(
        "--results",
        default="benchmarks/results/2025-11.json",
        help="Path to a benchmarks/results/*.json file.",
    )
    lb.set_defaults(func=_cmd_leaderboard)

    ls = sub.add_parser("list-systems", help="List registered systems.")
    ls.set_defaults(func=_cmd_list_systems)

    lts = sub.add_parser("list-test-sets", help="List registered test sets.")
    lts.set_defaults(func=_cmd_list_test_sets)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
