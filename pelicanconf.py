#!/usr/bin/env python

AUTHOR = "Carles Julià"
SITENAME = "Escric coses"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Madrid"

DEFAULT_LANG = "ca"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (
#     ("Pelican", "https://getpelican.com/"),
#     ("Python.org", "https://python.org/"),
#     ("Jinja2", "https://jinja.org/"),
# )
LINKS = ()

# Social widget
SOCIAL = (
    ("GitHub", "https://github.com/chaosct"),
    ("X", "https://x.com/chaosct"),
    ("LinkedIn", "https://www.linkedin.com/in/carles-juli%C3%A0-ph-d-b0bb5141/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = "notmyidea"

ARTICLE_PATHS = ["ca", "en"]
ARTICLE_URL = "{lang}/{slug}/"
ARTICLE_SAVE_AS = "{lang}/{slug}/index.html"
PAGE_PATHS = ["pages"]
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

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

# Language configuration
DEFAULT_LANG = "ca"
LOCALE = "ca_ES"
