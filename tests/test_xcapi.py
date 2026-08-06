"""Unit tests for the cached Xeno-canto client."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from orthoptera.xcapi.download import download_recording, recording_filename, recording_url
from orthoptera.xcapi.search import build_search_url, search_recordings


class FakeResponse:
    def __init__(self, content: bytes) -> None:
        self.content = content

    def __enter__(self) -> "FakeResponse":
        return self

    def __exit__(self, *args: object) -> None:
        return None

    def read(self) -> bytes:
        return self.content


class FakeOpener:
    def __init__(self, content: bytes) -> None:
        self.content = content
        self.calls: list[tuple[str, float]] = []

    def __call__(self, request: Any, timeout: float) -> FakeResponse:
        self.calls.append((request.full_url, timeout))
        return FakeResponse(self.content)


def test_build_search_url_encodes_query_and_api_key() -> None:
    url = build_search_url("grp:grasshoppers cnt:France", page=2, api_key="abc")

    assert url == (
        "https://xeno-canto.org/api/3/recordings?"
        "query=grp%3Agrasshoppers+cnt%3AFrance&page=2&key=abc"
    )


@pytest.mark.parametrize("query,page", [("", 1), ("   ", 1), ("grp:orthoptera", 0)])
def test_build_search_url_rejects_invalid_arguments(query: str, page: int) -> None:
    with pytest.raises(ValueError):
        build_search_url(query, page)


def test_search_caches_successful_json_response(tmp_path: Path) -> None:
    response = {"numRecordings": "1", "recordings": [{"id": "1"}]}
    opener = FakeOpener(json.dumps(response).encode())

    first_result = search_recordings("grp:orthoptera", tmp_path, opener=opener)
    second_result = search_recordings("grp:orthoptera", tmp_path, opener=opener)

    assert first_result == response
    assert second_result == response
    assert len(opener.calls) == 1
    assert not any("grp:orthoptera" in path.name for path in tmp_path.rglob("*"))


def test_download_caches_audio_and_does_not_overwrite_raw_recording(tmp_path: Path) -> None:
    recording = {
        "id": "42",
        "file": "//audio.xeno-canto.org/42/download",
        "file-name": "example.mp3",
    }
    opener = FakeOpener(b"audio bytes")
    destination_dir = tmp_path / "recordings"
    cache_dir = tmp_path / "cache"

    first_path = download_recording(recording, destination_dir, cache_dir, opener=opener)
    second_path = download_recording(recording, destination_dir, cache_dir, opener=opener)

    assert first_path == destination_dir / "XC42_example.mp3"
    assert second_path == first_path
    assert first_path.read_bytes() == b"audio bytes"
    assert len(opener.calls) == 1


def test_download_refuses_to_replace_existing_recording(tmp_path: Path) -> None:
    recording = {"id": "42", "file": "https://audio.xeno-canto.org/42/example.mp3"}
    destination_path = tmp_path / recording_filename(recording, recording_url(recording))
    destination_path.write_bytes(b"different bytes")

    with pytest.raises(FileExistsError):
        download_recording(recording, tmp_path, tmp_path / "cache", opener=FakeOpener(b"audio bytes"))


@pytest.mark.parametrize("file_url", ["", "http://example.org/a.mp3", "relative/a.mp3"])
def test_recording_url_requires_https(file_url: str) -> None:
    with pytest.raises(ValueError):
        recording_url({"id": "42", "file": file_url})
