#!/usr/bin/env python

from pathlib import Path
from runpy import run_path

globals().update(run_path(Path(__file__).with_name("pelicanconf.py")))

SITEURL = "https://blog.carlesjulia.com"
RELATIVE_URLS = False
