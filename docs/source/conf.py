# Configuration file for the Sphinx documentation builder.
import os
import sys

# -- Path setup --------------------------------------------------------------
# 如果你的 ariel_srt 包在 src 目录下，可以添加路径（可选）
# sys.path.insert(0, os.path.abspath('../../src'))

# -- Project information -----------------------------------------------------
project = 'ARIEL'
copyright = '2025, Yang Wanshuo, Yin Jun'
author = 'Yang Wanshuo, Yin Jun'

# The full version, including alpha/beta/rc tags
release = '0.1.0'


# -- General configuration ---------------------------------------------------
# 只保留 myst-nb，它已包含对 .md 和 .ipynb 的支持
extensions = [
    'myst_nb',               # 核心：支持 Markdown 和 Jupyter Notebook
    'sphinx_rtd_theme',      # 使用 Read the Docs 主题
]

# 设置主页面
master_doc = 'index'

# 支持的文件后缀
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
    '.ipynb': 'myst-nb',
}

# 语言
language = 'en'

# 不要尝试执行 notebook（关键！避免内核错误和加速构建）
nb_execution_mode = "off"

# 可选：如果你希望缓存执行结果（开发时）
# nb_execution_cache_path = './_build/.jupyter_cache'

# 忽略某些文件
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '**.ipynb_checkpoints'
]


# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'

# HTML 输出选项
html_static_path = ['_static']

# 在侧边栏显示当前页的章节
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
}

# -- Internationalization ----------------------------------------------------
gettext_compact = False