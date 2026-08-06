"""Tools for reproducible analysis of Orthoptera acoustic recordings."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("orthoptera")
except PackageNotFoundError:
    __version__ = "0.1.0"
