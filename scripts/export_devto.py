#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

CONTENT_ROOT = Path("content")
EXPORT_ROOT = Path("exports") / "devto"
LANGS = ("ca", "en")


def export_lang(lang: str) -> None:
    src_dir = CONTENT_ROOT / lang
    dst_dir = EXPORT_ROOT / lang
    dst_dir.mkdir(parents=True, exist_ok=True)

    for source_path in sorted(src_dir.glob("*.md")):
        target_path = dst_dir / source_path.name
        shutil.copyfile(source_path, target_path)


def main() -> int:
    for lang in LANGS:
        export_lang(lang)
    print("Exported dev.to files to exports/devto/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
