"""Rewrite relative Markdown links so Pelican resolves them as article URLs."""

from __future__ import annotations

from urllib.parse import urlparse

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


def _should_rewrite(href: str | None) -> bool:
    if not href or href.startswith(("{", "#", "/", "mailto:", "tel:")):
        return False

    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return False

    return parsed.path.endswith(".md")


class InternalMarkdownLinkTreeprocessor(Treeprocessor):
    def run(self, root):  # type: ignore[override]
        for element in root.iter("a"):
            href = element.get("href")
            if _should_rewrite(href):
                element.set("href", f"{{filename}}{href}")
        return root


class InternalMarkdownLinkExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            InternalMarkdownLinkTreeprocessor(md),
            "internal_markdown_links",
            priority=15,
        )


def makeExtension(**kwargs):
    return InternalMarkdownLinkExtension(**kwargs)
