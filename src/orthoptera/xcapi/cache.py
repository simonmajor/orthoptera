"""Deterministic filesystem caching for Xeno-canto HTTP responses."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


def response_cache_path(cache_dir: Path, request_url: str, suffix: str) -> Path:
    """Return the cache path for a URL without exposing it in a filename."""
    if not suffix.startswith("."):
        raise ValueError("suffix must start with a full stop")
    return cache_dir / f"{sha256(request_url.encode('utf-8')).hexdigest()}{suffix}"


def load_cached_response(cache_path: Path) -> bytes | None:
    """Return cached bytes, or ``None`` when no response has been cached."""
    if not cache_path.is_file():
        return None
    return cache_path.read_bytes()


def store_cached_response(cache_path: Path, content: bytes) -> None:
    """Atomically store a successful HTTP response."""
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = cache_path.with_suffix(f"{cache_path.suffix}.tmp")
    temporary_path.write_bytes(content)
    temporary_path.replace(cache_path)
