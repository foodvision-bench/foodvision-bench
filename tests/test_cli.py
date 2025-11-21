"""Smoke tests for the CLI."""
from __future__ import annotations

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


def test_version_flag(capsys):
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])
    assert exc_info.value.code == 0
    out = capsys.readouterr().out
    assert "foodvision-bench" in out
