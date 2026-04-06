#!/usr/bin/env python3
"""Export original Markdown sources for LLM-friendly consumption.

Copies article Markdown from content/<lang>/<category>/<slug>.md to:
  output/llm/<lang>/<slug>/index.md

The content is copied 1:1 (including YAML frontmatter), by design.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def extract_slug_and_lang(path: Path) -> tuple[str, str]:
    # Expected: content/<lang>/<category>/<slug>.md
    parts = path.parts
    try:
        idx = parts.index("content")
    except ValueError as e:
        raise ValueError(f"Unexpected path (no content/): {path}") from e

    if len(parts) < idx + 4:
        raise ValueError(f"Unexpected content path depth: {path}")

    lang = parts[idx + 1]
    slug = path.stem
    return slug, lang


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    content_dir = repo_root / "content"
    out_dir = repo_root / "output" / "llm"

    md_files = sorted(content_dir.rglob("*.md"))
    if not md_files:
        print("No markdown files found under content/")
        return 0

    out_dir.mkdir(parents=True, exist_ok=True)

    copied = 0
    for src in md_files:
        # Skip non-article markdown if any appear later
        # (currently all are articles)
        slug, lang = extract_slug_and_lang(src)

        dest = out_dir / lang / slug / "index.md"
        dest.parent.mkdir(parents=True, exist_ok=True)

        # Copy 1:1
        shutil.copyfile(src, dest)
        copied += 1

        # Basic sanity: frontmatter present (your current content uses it)
        text = dest.read_text(encoding="utf-8")
        if not FRONTMATTER_RE.search(text):
            print(f"WARNING: no YAML frontmatter detected in {src}")

    print(f"Exported {copied} markdown files to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
