#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

CONTENT_ROOT = Path("content")
DOCS_ROOT = Path("docs")
LANGS = ("ca", "en")


def strip_front_matter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return text
    return parts[1].lstrip("\n")


def render_lang(lang: str) -> None:
    src_dir = CONTENT_ROOT / lang
    dst_dir = DOCS_ROOT / lang
    dst_dir.mkdir(parents=True, exist_ok=True)

    for source_path in sorted(src_dir.glob("*.md")):
        if source_path.name == "index.md":
            continue
        target_path = dst_dir / source_path.name
        text = source_path.read_text(encoding="utf-8")
        target_path.write_text(strip_front_matter(text), encoding="utf-8")


def main() -> int:
    for lang in LANGS:
        render_lang(lang)
    print("Rendered docs from content/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
