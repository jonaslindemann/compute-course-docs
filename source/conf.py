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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Scientific Programming in Python and Fortran'
copyright = '2022-2026, Jonas Lindemann'
author = 'Jonas Lindemann'

# The full version, including alpha/beta/rc tags
release = '0.4'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'shibuya'

html_title = 'Scientific Programming in Python and Fortran'
html_show_sourcelink = True
html_baseurl = 'https://compute-course-docs.readthedocs.io/'

html_theme_options = {
    # Accent colour used for links, active navigation entries and highlights
    'accent_color': 'blue',

    # Show a GitHub link in the header
    'github_url': 'https://github.com/jonaslindemann/compute-course-docs',

    # Extra links in the top navigation bar
    'nav_links': [
        {'title': 'Python', 'url': 'python_lectures'},
        {'title': 'Fortran', 'url': 'fortran_lectures'},
        {'title': 'Project', 'url': 'project_assignment'},
    ],

    # Sidebar navigation behaviour
    'globaltoc_expand_depth': 1,
    'toctree_collapse': True,
}

# Used by the theme to build "Edit this page" links
html_context = {
    'source_type': 'github',
    'source_user': 'jonaslindemann',
    'source_repo': 'compute-course-docs',
    'source_version': 'main',
    'source_docs_path': '/source/',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom stylesheet, loaded after the theme's own CSS
html_css_files = ['custom.css']
