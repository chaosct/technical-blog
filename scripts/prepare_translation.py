#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def split_front_matter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return "", text
    front_matter = parts[0].removeprefix("---\n")
    body = parts[1]
    return front_matter.strip(), body.lstrip("\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a translation stub for an article."
    )
    parser.add_argument("--slug", required=True)
    parser.add_argument("--from-lang", default="ca")
    parser.add_argument("--to-lang", default="en")
    args = parser.parse_args()

    source_path = Path("content") / args.from_lang / "blog" / f"{args.slug}.md"
    if not source_path.exists():
        raise SystemExit(f"Missing source: {source_path}")

    target_path = Path("content") / args.to_lang / "blog" / f"{args.slug}.md"
    if target_path.exists():
        raise SystemExit(f"Target already exists: {target_path}")

    text = source_path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text)
    note = (
        "<!-- TODO: Translate this article to English. Replace the body and update\n"
        "the title/description in the front matter. -->\n\n"
    )

    if front_matter:
        output = f"---\n{front_matter}\n---\n\n{note}{body}"
    else:
        output = f"{note}{body}"

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(output, encoding="utf-8")
    print(f"Created {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
