# Borrowing heavily from Jason Moore's site:
# https://github.com/mechmotum/mechmotum.github.io/

#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import yaml

AUTHOR = 'Robert Lanzafame'
SITENAME = 'Robert Lanzafame'
SITEURL = ""
SOURCEURL = 'https://github.com/rlanzafame/rlanzafame.github.io'

PATH = "content"
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'

## Jason Moore's settings

# This sets the default pages to be top level items and articles to be under
# /blog/.
INDEX_SAVE_AS = 'blog/index.html'

# All blog posts will have slugs that match the file name.
PATH_METADATA = '(?P<path_no_ext>.*)\..*'  # regex to grab file name without ext
ARTICLE_URL = 'blog/{path_no_ext}.html'
ARTICLE_SAVE_AS = 'blog/{path_no_ext}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
PAGE_ORDER_BY = 'sortorder'

MENUITEMS = [('Blog', '/blog/')]

## Pelican initialization settings
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

## More of Jason Moore's settings
try:
    with open('config.yml', 'r') as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)
except IOError:
    THEME = ''
    PLUGIN_PATHS = ['']
else:
    THEME = config_data['THEME_PATH']
    PLUGIN_PATHS = config_data['PLUGIN_PATHS']
    if isinstance(PLUGIN_PATHS, type('')):
        PLUGIN_PATHS = [PLUGIN_PATHS]
print(THEME, PLUGIN_PATHS)
## THEME

# Alchemy theme settings
OS_SEP = os.sep
# DISQUS_SITENAME = "blank"
SITESUBTITLE = 'Personal Website'
# SITEIMAGE = 'https://rlanzafame.github.io/assets/images/sailboat-sloop.svg'
# INSTITUTEIMAGE should bee 100px in height
INSTITUTIONIMAGE = 'https://rlanzafame.github.io/assets/logos/tud-233x100.png'
DESCRIPTION = ''
# pelican-alchemy removed the original theme.css, so bring it back.
THEME_CSS_OVERRIDES = ['theme/css/origtheme.css']
REPO_URL = 'https://github.com/rlanzafame/rlanzafame.github.io'
# TODO : Fix the template so that if this isn't declared it still builds.
EXCLUDED_CATEGORIES = []

#GOOGLE_ANALYTICS = ''
#DISQUS_SITENAME = ''

## PLUGINS

PLUGINS = ['render_math', 'extract_toc']