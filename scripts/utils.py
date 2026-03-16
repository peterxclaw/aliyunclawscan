"""Utility functions for aliclawscan."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterator, Optional

SKIP_DIRS = {
    "node_modules", ".git", "dist", "build", ".next", "coverage",
    "__pycache__", ".turbo", ".cache", ".output", "vendor",
}

SCANNABLE_EXTENSIONS = {
    ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".mts", ".cts",
    ".json", ".yaml", ".yml", ".toml", ".env", ".sh", ".bash",
    ".py", ".swift", ".kt", ".kts", ".gradle",
}

MAX_FILE_BYTES = 2 * 1024 * 1024  # 2 MB


def is_test_file(path: Path) -> bool:
    """Check if file is a test file."""
    path_str = str(path).lower()
    return any(x in path_str for x in [".test.", ".spec.", "/tests/", "/__tests__/", "/fixtures/"])


def walk_files(
    root: Path,
    extensions: set[str] | None = None,
    exclude_dirs: set[str] | None = None,
    exclude_tests: bool = False,
) -> Iterator[Path]:
    """Yield files under *root*, skipping excluded directories."""
    skip = exclude_dirs or SKIP_DIRS
    exts = extensions or SCANNABLE_EXTENSIONS
    for child in sorted(root.iterdir()):
        if child.name.startswith(".") and child.is_dir():
            continue
        if child.is_dir():
            if child.name in skip:
                continue
            yield from walk_files(child, exts, skip, exclude_tests)
        elif child.is_file() and child.suffix in exts:
            if exclude_tests and is_test_file(child):
                continue
            yield child


def read_file_safe(path: Path, max_bytes: int = MAX_FILE_BYTES) -> str:
    """Read a file, returning empty string on failure or if too large."""
    try:
        if path.stat().st_size > max_bytes:
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, UnicodeDecodeError):
        return ""


def truncate_evidence(text: str, max_len: int = 120) -> str:
    """Truncate evidence string, matching skill-scanner.ts convention."""
    text = text.strip()
    if len(text) <= max_len:
        return text
    return text[:max_len] + "…"


def redact_secret(text: str) -> str:
    """Mask the middle of a potential secret value."""
    if len(text) <= 8:
        return "***"
    return text[:4] + "***" + text[-4:]


def parse_openclaw_audit_json(json_str: str) -> dict:
    """Parse JSON output from `openclaw security audit --deep --json`."""
    try:
        data = json.loads(json_str)
        if isinstance(data, dict) and "findings" in data:
            return data
    except (json.JSONDecodeError, TypeError):
        pass
    return {"summary": {}, "findings": []}
