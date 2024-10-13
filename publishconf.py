# Borrowing heavily from Jason Moore's site:
# https://github.com/mechmotum/mechmotum.github.io/

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals # from Jason Moore's site

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

THEME = "pelican-alchemy/alchemy"
PLUGIN_PATHS = "pelican-plugins"

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = "https://rlanzafame.github.io"
RELATIVE_URLS = False

# FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
