"""Download Xeno-canto recordings while preserving cached raw responses."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from .cache import load_cached_response, response_cache_path, store_cached_response
from .search import USER_AGENT

Opener = Callable[[Request, float], Any]


def recording_url(recording: Mapping[str, Any]) -> str:
    """Return the HTTPS download URL from a Xeno-canto recording result."""
    file_url = recording.get("file")
    if not isinstance(file_url, str) or not file_url:
        raise ValueError("recording must contain a non-empty 'file' URL")
    if file_url.startswith("//"):
        return f"https:{file_url}"
    if urlparse(file_url).scheme != "https":
        raise ValueError("recording file URL must use HTTPS")
    return file_url


def recording_filename(recording: Mapping[str, Any], download_url: str) -> str:
    """Create a safe, stable filename from a recording identifier and URL."""
    recording_id = recording.get("id")
    if not isinstance(recording_id, str) or not recording_id:
        raise ValueError("recording must contain a non-empty 'id'")
    file_name = recording.get("file-name")
    remote_name = (
        Path(file_name).name
        if isinstance(file_name, str)
        else Path(urlparse(download_url).path).name
    )
    if not remote_name:
        raise ValueError("recording file URL must include a filename")
    return f"XC{recording_id}_{remote_name}"


def download_recording(
    recording: Mapping[str, Any],
    destination_dir: Path,
    cache_dir: Path,
    *,
    timeout: float = 30.0,
    opener: Opener = urlopen,
) -> Path:
    """Download a recording and return its raw, immutable destination path."""
    download_url = recording_url(recording)
    filename = recording_filename(recording, download_url)
    cache_path = response_cache_path(cache_dir / "downloads", download_url, ".audio")
    content = load_cached_response(cache_path)
    if content is None:
        request = Request(download_url, headers={"User-Agent": USER_AGENT})
        with opener(request, timeout=timeout) as response:
            content = response.read()
        store_cached_response(cache_path, content)

    destination_path = destination_dir / filename
    if destination_path.exists() and destination_path.read_bytes() != content:
        raise FileExistsError(f"refusing to overwrite existing file: {destination_path}")
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    if not destination_path.exists():
        destination_path.write_bytes(content)
    return destination_path
