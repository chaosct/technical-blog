"""Embed standalone YouTube links as responsive iframes."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse
from xml.etree.ElementTree import Element

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


def _youtube_embed_url(url: str | None) -> str | None:
    if not url:
        return None

    parsed = urlparse(url)
    host = parsed.netloc.lower()
    video_id: str | None = None

    if host in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.strip("/") or None
    elif host in {"youtube.com", "www.youtube.com", "m.youtube.com"}:
        if parsed.path == "/watch":
            video_id = parse_qs(parsed.query).get("v", [None])[0]
        elif parsed.path.startswith(("/embed/", "/shorts/")):
            video_id = parsed.path.split("/", 2)[2] or None

    if not video_id:
        return None

    return f"https://www.youtube.com/embed/{video_id}?feature=oembed"


class YouTubeEmbedTreeprocessor(Treeprocessor):
    def run(self, root):  # type: ignore[override]
        for index, element in enumerate(list(root)):
            if element.tag != "p":
                continue

            embed_url = None
            text_content = (element.text or "").strip()
            if len(element) == 0 and text_content:
                embed_url = _youtube_embed_url(text_content)
            elif (
                element.text in (None, "")
                and len(element) == 1
                and element[0].tag == "a"
            ):
                link = element[0]
                if link.tail not in (None, ""):
                    continue

                href = link.get("href")
                if (link.text or "").strip() != (href or "").strip():
                    continue

                embed_url = _youtube_embed_url(href)

            if not embed_url:
                continue

            wrapper = Element(
                "div",
                {
                    "class": "video-embed video-embed-youtube",
                    "style": (
                        "position: relative; "
                        "width: 100%; "
                        "padding-bottom: 56.25%; "
                        "height: 0; "
                        "margin: 1.5rem 0;"
                    ),
                },
            )
            iframe = Element(
                "iframe",
                {
                    "src": embed_url,
                    "title": "YouTube video",
                    "frameborder": "0",
                    "loading": "lazy",
                    "referrerpolicy": "strict-origin-when-cross-origin",
                    "allow": (
                        "accelerometer; autoplay; clipboard-write; "
                        "encrypted-media; gyroscope; picture-in-picture; web-share"
                    ),
                    "allowfullscreen": "allowfullscreen",
                    "style": (
                        "position: absolute; "
                        "inset: 0; "
                        "width: 100%; "
                        "height: 100%; "
                        "border: 0;"
                    ),
                },
            )
            wrapper.append(iframe)
            root[index] = wrapper

        return root


class YouTubeEmbedExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(
            YouTubeEmbedTreeprocessor(md),
            "youtube_embed",
            priority=8,
        )


def makeExtension(**kwargs):
    return YouTubeEmbedExtension(**kwargs)
