# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'unstable_baselines'
copyright = '2023, x35f'
author = 'x35f'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Markdown Support --------------------------------------------------------
from recommonmark.parser import CommonMarkParser
source_parsers = {
	'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

# -- Theme -------------------------------------------------------------------
import sphinx_rtd_theme
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

import os
import sys
# Make sure spinup is accessible without going through setup.py
dirname = os.path.dirname
sys.path.insert(0, dirname(dirname(__file__)))