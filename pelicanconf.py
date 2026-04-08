#!/usr/bin/env python

AUTHOR = "Carles Julià"
SITENAME = "Escric coses"
SITESUBTITLE = "Bloc tècnic de Carles Julià"
SITEURL = "https://blog.carlesjulia.com"

PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "ca"
LOCALE = "ca_ES"

# Plugins
PLUGINS = ["sitemap"]

# Article configuration
ARTICLE_PATHS = ["ca", "en"]
PATH_METADATA = r"(?P<lang>[a-z]{2})/(?P<category>.*)/(?P<slug>.*)\..*"
SLUGIFY_SOURCE = "basename"

# URL settings
ARTICLE_URL = "{lang}/{slug}/"
ARTICLE_SAVE_AS = "{lang}/{slug}/index.html"
TRANSLATION_URL = "{lang}/{slug}/"
TRANSLATION_SAVE_AS = "{lang}/{slug}/index.html"

# Page configuration
PAGE_PATHS = ["pages"]
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Feed generation
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Sitemap
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.8, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "weekly", "pages": "monthly"},
}

# Theme
THEME = "notmyidea"
THEME_TEMPLATES_OVERRIDES = ["theme_overrides"]

# Static paths
STATIC_PATHS = [
    "images",
    "extra/favicon.ico",
    "extra/robots.txt",
    "extra/llms.txt",
    "extra/llm/ca/index.html",
    "extra/llm/en/index.html",
]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/llms.txt": {"path": "llms.txt"},
    "extra/llm/ca/index.html": {"path": "llm/ca/index.html"},
    "extra/llm/en/index.html": {"path": "llm/en/index.html"},
}
DEFAULT_SOCIAL_IMAGE = "images/social-card-default.png"

# Markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown_extensions.internal_links": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
    },
    "output_format": "html5",
}

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/chaosct"),
    ("X", "https://x.com/chaosct"),
    ("LinkedIn", "https://www.linkedin.com/in/carles-juli%C3%A0-ph-d-b0bb5141/"),
)

DEFAULT_PAGINATION = 10
LINKS = ()
