#!/usr/bin/env python

AUTHOR = "Carles Julià"
SITENAME = "Escric coses"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "ca"
LOCALE = "ca_ES"

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
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = "notmyidea"

# Static paths
STATIC_PATHS = ["images", "extra/favicon.ico"]
EXTRA_PATH_METADATA = {"extra/favicon.ico": {"path": "favicon.ico"}}

# Markdown extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
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
