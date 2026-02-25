#!/usr/bin/env python3
from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

TEMPLATES = {
    "ca": Path("templates/article_ca.md"),
    "en": Path("templates/article_en.md"),
}


def render_template(template_path: Path, title: str, description: str) -> str:
    text = template_path.read_text(encoding="utf-8")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    return (
        text.replace("{{TITLE}}", title)
        .replace("{{DESCRIPTION}}", description)
        .replace("{{DATE}}", now)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create a new article file from a template."
    )
    parser.add_argument("--lang", choices=["ca", "en"], default="ca")
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--description", default="")
    args = parser.parse_args()

    template_path = TEMPLATES[args.lang]
    if not template_path.exists():
        raise SystemExit(f"Missing template: {template_path}")

    output_dir = Path("content") / args.lang / "blog"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{args.slug}.md"

    if output_path.exists():
        raise SystemExit(f"File already exists: {output_path}")

    description = args.description or f"Article about {args.title}."
    output_path.write_text(
        render_template(template_path, args.title, description), encoding="utf-8"
    )
    print(f"Created {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
