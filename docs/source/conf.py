# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'LSD Sphinx'
copyright = '2024, Lorraine J. Hwang'
author = 'Lorraine J. Hwang'

# The full version, including alpha/beta/rc tags
release = '0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinxcontrib.bibtex",
    "myst_parser"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_logo = "_static/background16-9offset.jpg"

html_theme_options = {
   "collapse_navigation": True,
    "navigation_depth": 3,
    "show_toc_level": 3,
      "logo": {
        "text": "Legacy Seismic Data",
        
    },
    "home_page_in_toc": True,
    "primary_sidebar_end": "navbar_end.html",
    "repository_url": "https://github.com/ljhwang/LSD_Sphinx/",
    "repository_branch": "main",
    "path_to_docs":"docs/source/",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Add bibtex and generate a bibliography
bibtex_bibfiles = ["references.bib"]
bibtex_default_style = "alpha"
bibtex_reference_style = "author_year"

# If true, figures, tables and code-blocks are automatically numbered if they have a caption. 
numfig = True