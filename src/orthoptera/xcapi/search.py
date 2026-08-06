"""Search the public Xeno-canto recordings API."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .cache import load_cached_response, response_cache_path, store_cached_response

API_URL = "https://xeno-canto.org/api/3/recordings"
USER_AGENT = "orthoptera/0.1.0"

Opener = Callable[[Request, float], Any]


def build_search_url(query: str, page: int = 1, api_key: str | None = None) -> str:
    """Build a public API request URL for a Xeno-canto query."""
    if not query.strip():
        raise ValueError("query must not be empty")
    if page < 1:
        raise ValueError("page must be at least 1")

    parameters: dict[str, str | int] = {"query": query, "page": page}
    if api_key is not None:
        parameters["key"] = api_key
    return f"{API_URL}?{urlencode(parameters)}"


def search_recordings(
    query: str,
    cache_dir: Path,
    *,
    page: int = 1,
    api_key: str | None = None,
    timeout: float = 30.0,
    opener: Opener = urlopen,
) -> dict[str, Any]:
    """Return one cached-or-fresh page of Xeno-canto search results.

    ``query`` uses Xeno-canto's public API query syntax.  A supplied API key is
    included only in the request URL; cache filenames are hashes and therefore
    do not reveal it.
    """
    request_url = build_search_url(query, page, api_key)
    cache_path = response_cache_path(cache_dir / "search", request_url, ".json")
    cached_content = load_cached_response(cache_path)
    if cached_content is None:
        request = Request(request_url, headers={"User-Agent": USER_AGENT})
        with opener(request, timeout=timeout) as response:
            cached_content = response.read()
        store_cached_response(cache_path, cached_content)

    result = json.loads(cached_content)
    if not isinstance(result, dict):
        raise ValueError("Xeno-canto search response must be a JSON object")
    return result
