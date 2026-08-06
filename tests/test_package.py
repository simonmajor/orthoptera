"""Smoke tests for the installed package layout."""

from importlib import import_module

import orthoptera


def test_package_exposes_version() -> None:
    assert orthoptera.__version__ == "0.1.0"


def test_package_submodules_are_importable() -> None:
    for module in (
        "analysis",
        "database",
        "signal",
        "xcapi",
    ):
        import_module(f"orthoptera.{module}")
