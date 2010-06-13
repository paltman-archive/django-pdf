# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath(os.curdir))
sys.path.append(os.path.abspath(os.pardir))
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
source_suffix = '.txt'
master_doc = 'index'

project = u'django-pdf'
copyright = u'2010, Patrick Altman'
version = '1.0.0'
release = '1.0.0'

exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
htmlhelp_basename = 'django-pdfdoc'

latex_documents = [
  ('index', 'django-pdf.tex', u'django-pdf Documentation',
   u'Patrick Altman', 'manual'),
]

man_pages = [
    ('index', 'django-pdf', u'django-pdf Documentation',
     [u'Patrick Altman'], 1)
]
