# Configuration file for the Sphinx documentation builder.

# -- Project information
project = u'RCIC'
copyright = u'2019-2026, The Regents of the University of California'
author = u'RCIC'

version = 'latest'
release = '1.0.0'
# use same |release| as |version|
#release = version

# add path to python code snippets
import sys
import os
sys.path.insert(0, os.path.abspath('src'))

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']
templates_path = ['_templates']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# The suffixes of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# for roles creation
rst_prolog = """
.. include:: /roles.txt
.. default-role::

"""

# Currently line below is not needed as breadcrumbs is overwritten in _templates 
# if breadcrumbs are enabled but dont want to show View the source link at the top
#html_show_sourcelink = False

# ---------------------------------------------
#      Options for HTML output
# ---------------------------------------------

# this is a theme that is used to produce html output
html_theme = 'sphinx_rtd_theme'

# custom dir for storing files
html_static_path = [ '_static', 'pdfs']

# custom css file relative to custom dir
html_css_files = [ 'css/rcic.css','css/jquery.dataTables.min.css']

# custom js files relative to custom dir
html_js_files = ['js/jquery.dataTables.min.js', 'js/main.js',]

# top sidebar image image (relative to the dir where this file is)
html_logo = 'images/rcic-logo.png'

# 'Last updated on:' timestamp is inserted at every page footer using the given strftime format.
# If want to remove (really dont) set to ''
html_last_updated_fmt = '%Y-%m-%d'

# Disable the self-link to the page title of every page
# This is important for accessibility
html_permalinks = False

# currently used options
html_theme_options = {
    # use this to show only logo on top of the side bar without home button link 
    'logo_only': True,
    # accessibility: this keeps navigation menu opening only to one level
    'navigation_depth': 2,
    # prevents injecting  default (accesskey issue for accessibility) buttons.
    'prev_next_buttons_location': 'None',
    # top portion of sidebar background
    #'style_nav_header_background': '#353130',
    #'display_version': True,
    #'prev_next_buttons_location': 'both',
    #'style_external_links': False,
    # Toc options
    #'collapse_navigation': True,
    #'sticky_navigation': True,
    #'includehidden': True,
    #'titles_only': False
}

# enable figure auto numbering
numfig = True

# =========== start overwrite mailto: directives 
# sphinx creates <span> tags in mailto links which confuse
# accessibility checkers into flagging  such links as duplicate
from docutils import nodes
from sphinx.writers.html import HTML5Translator

class CleanEmailTranslator(HTML5Translator):
    def visit_reference(self, node):
        # If it's a mailto link, prevent the theme from splitting it
        if node.get('refuri', '').startswith('mailto:'):
            atts = {'class': 'reference external', 'href': node['refuri']}
            self.body.append(self.starttag(node, 'a', '', **atts))
        else:
            super().visit_reference(node)

    def depart_reference(self, node):
        if node.get('refuri', '').startswith('mailto:'):
            self.body.append('</a>')
        else:
            super().depart_reference(node)

def setup(app):
    # This forces Sphinx to use our custom 'clean' translator
    app.set_translator('html', CleanEmailTranslator)
# =========== end overwrite mailto: directives 
