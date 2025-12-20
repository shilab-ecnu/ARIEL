# Configuration file for the Sphinx documentation builder.

project = 'ARIEL'
copyright = '2025, Yang Wanshuo, Yin Jun'
author = 'Yang Wanshuo, Yin Jun'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

extensions = [
    'myst_nb',               
    'sphinx_rtd_theme',      
]

master_doc = 'index'

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.ipynb': 'myst-nb',
}

language = 'en'

# Do not run notebook
# nb_execution_mode = "off"

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints'
]


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = []

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# -- Internationalization ----------------------------------------------------
gettext_compact = False