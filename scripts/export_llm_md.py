#!/usr/bin/env python3
"""Export original Markdown sources for LLM-friendly consumption.

Copies article Markdown from content/<lang>/<category>/<slug>.md to:
  output/llm/<lang>/<slug>/index.md

Also generates:
  output/llm/<lang>/index.html

The content is copied 1:1 (including YAML frontmatter), by design.
"""

from __future__ import annotations

import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)
STATUS_RE = re.compile(r"^status:\s*(.+?)\s*$", re.M)
DATE_RE = re.compile(r"^date:\s*(.+?)\s*$", re.M)


@dataclass(frozen=True)
class ArticleExport:
    slug: str
    lang: str
    status: str | None
    date: datetime | None


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


def extract_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_RE.search(text)
    if not match:
        return None
    return match.group(1)


def extract_field(frontmatter: str, pattern: re.Pattern[str]) -> str | None:
    match = pattern.search(frontmatter)
    if not match:
        return None
    return match.group(1).strip().strip("\"'")


def parse_date(raw_date: str | None) -> datetime | None:
    if not raw_date:
        return None

    normalized = raw_date.strip().replace(" ", "T", 1)
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        return None


def render_index(lang: str, articles: list[ArticleExport]) -> str:
    labels = {
        "ca": {
            "title": "LLM Markdown index (ca)",
            "heading": "LLM Markdown index (Català)",
            "intro": (
                "Aquesta pàgina enllaça a les versions Markdown originals "
                "(còpia 1:1 del <code>content/</code>) pensades per a consum "
                "per LLMs."
            ),
            "note": (
                "Nota: l'índex només enumera articles publicats, tot i que hi "
                "poden existir altres exports Markdown a partir de fitxers font "
                "presents a <code>content/</code>."
            ),
        },
        "en": {
            "title": "LLM Markdown index (en)",
            "heading": "LLM Markdown index (English)",
            "intro": (
                "This page links to the original source Markdown exports "
                "(1:1 copy from <code>content/</code>), meant for LLM "
                "consumption."
            ),
            "note": None,
        },
    }
    text = labels.get(lang, labels["en"])

    article_items = "\n".join(
        f'      <li><a href="/llm/{lang}/{article.slug}/index.md">{article.slug}</a></li>'
        for article in articles
    )

    note_html = ""
    if text["note"]:
        note_html = f"""
    <p>
      {text["note"]}
    </p>"""

    return f"""<!doctype html>
<html lang="{lang}">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{text["title"]}</title>
    <meta name="robots" content="noindex" />
  </head>
  <body>
    <h1>{text["heading"]}</h1>
    <p>
      {text["intro"]}
    </p>
    <ul>
{article_items}
    </ul>{note_html}
  </body>
</html>
"""


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
    published_by_lang: dict[str, list[ArticleExport]] = {}
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
        frontmatter = extract_frontmatter(text)
        if not frontmatter:
            print(f"WARNING: no YAML frontmatter detected in {src}")
            continue

        status = extract_field(frontmatter, STATUS_RE)
        article = ArticleExport(
            slug=slug,
            lang=lang,
            status=status,
            date=parse_date(extract_field(frontmatter, DATE_RE)),
        )
        if article.status == "published":
            published_by_lang.setdefault(lang, []).append(article)

    for lang, articles in published_by_lang.items():
        index_path = out_dir / lang / "index.html"
        sorted_articles = sorted(
            articles,
            key=lambda article: (
                article.date is not None,
                article.date or datetime.min,
                article.slug,
            ),
            reverse=True,
        )
        index_path.write_text(
            render_index(lang, sorted_articles),
            encoding="utf-8",
        )

    print(f"Exported {copied} markdown files to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
