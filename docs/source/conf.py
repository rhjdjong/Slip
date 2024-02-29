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

import pkg_resources

_sources = [
    os.path.abspath(os.path.join('..', '..', 'src')),
    os.path.abspath(os.path.join('..', '..', 'examples')),
]
sys.path[0:0] = _sources


# -- Project information -----------------------------------------------------

project = 'sliplib'
copyright = '2020, Ruud de Jong'
author = 'Ruud de Jong'

try:
    # The full version, including alpha/beta/rc tags
    release = pkg_resources.get_distribution(f'{project}').version
except pkg_resources.DistributionNotFound:
    print(f'To build the documentation, the distribution information of {project}')
    print('has to be available. Either install the package into your')
    print('development environment or run "setup.py develop" or "pip install -e"')
    print('to setup the metadata. A virtual environment is recommended!')
    sys.exit(1)
del pkg_resources

version = '.'.join(release.split('.')[:2])  # version contains major.minor.


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc.typehints',
]

autoclass_content = 'both'
autodoc_typehints = 'description'
add_module_names = False
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}

napoleon_use_rtype = True

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
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
