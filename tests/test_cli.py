"""Smoke tests for the CLI."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from foodvision_bench.cli import main


def test_list_systems_smoke(capsys):
    rc = main(["list-systems"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "clip-vit-l" in out


def test_list_test_sets_smoke(capsys):
    rc = main(["list-test-sets"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "mini-180" in out


def test_leaderboard_renders(tmp_path, capsys):
    # Regression test: MAPE must sort ascending (lower is better).
    results = {
        "entries": [
            {"system": "A", "mape_kcal": 0.20, "top_1": 0.5, "source": "open-source"},
            {"system": "B", "mape_kcal": 0.10, "top_1": 0.8, "source": "vendor"},
        ],
    }
    path: Path = tmp_path / "results.json"
    path.write_text(json.dumps(results))
    rc = main(["leaderboard", "--results", str(path)])
    assert rc == 0
    out = capsys.readouterr().out
    assert out.index("B") < out.index("A")


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])
    assert exc_info.value.code == 0
    out = capsys.readouterr().out
    assert "foodvision-bench" in out
