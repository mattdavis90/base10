# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../')

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx']

intersphinx_mapping = {'python': ('https://docs.python.org/2.7/',
                                  'https://docs.python.org/2.7/objects.inv'),}

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = 'base10'
copyright = '2016, Matt Davis'

import base10
release = base10.__version__
version = '.'.join(release.split('.')[0:1])

exclude_patterns = ['_build']
add_function_parentheses = True
add_module_names = True
show_authors = True
pygments_style = 'sphinx'
modindex_common_prefix = ['base10']
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'base10doc'
