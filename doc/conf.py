# -*- coding: utf-8 -*-
#
# conf.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

"""
Readthedocs configuration file
------------------------------

Use:
sphinx-build -c ../extras/help_generator -b html . _build/html

"""

import sys
import os


import pip

# pip.main(['install', 'Sphinx==1.5.6'])
# pip.main(['install', 'sphinx-gallery'])

# import sphinx_gallery
import subprocess

# import shlex
# import recommonmark

from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify
from subprocess import check_output, CalledProcessError
from mock import Mock as MagicMock

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('..'))
#sys.path.insert(0, os.path.abspath('./../topology'))
#sys.path.insert(0, os.path.abspath('./../pynest/'))
sys.path.insert(0, os.path.abspath('./../pynest/nest'))

for p in sys.path:
    print(p)

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser
}

# -- Checking for pandoc --------------------------------------------------

try:
    print(check_output(['pandoc', '--version']))
except CalledProcessError:
    print("No pandoc on %s" % os.environ['PATH'])


for dirpath, dirnames, files in os.walk(os.path.dirname(__file__)):
    for f in files:
        if f.endswith('.md'):
            ff = os.path.join(dirpath, f)
            print(ff)
            fb = os.path.basename(f)[:-3]
            print(fb)
            fo = fb + ".rst"
            args = ['pandoc', ff, '-o', fo]
            # check_output(args)
            # check_output(args)

# -- General configuration ------------------------------------------------
#autodoc_mock_imports = ["pynestkernel", "scipy", "numpy", "matplotlib", "pandas"]
# import errors on libraries that depend on C modules
# http://blog.rtwilson.com/how-to-make-your-sphinx-documentation-compile-with-readthedocs-when-youre-using-numpy-and-scipy/
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
            return MagicMock()


MOCK_MODULES = ['numpy', 'scipy', 'matplotlib', 'matplotlib.pyplot', 'pandas']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = [
#    'sphinx.ext.autodoc',
#    'sphinx.ext.napoleon',
#    'sphinx.ext.autosummary',
#    'sphinx.ext.doctest',
#    'sphinx.ext.intersphinx',
#    'sphinx.ext.todo',
#    'sphinx.ext.coverage',
#    'sphinx.ext.mathjax',
#    'sphinx_gallery.gen_gallery',
# ]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
]

# sphinx_gallery_conf = {
#    'doc_module': ('sphinx_gallery', 'numpy'),
#    # path to your examples scripts
#    'examples_dirs': '../pynest/examples',
#    # path where to save gallery generated examples
#    'gallery_dirs': 'auto_examples',
#    'backreferences_dir': False
# }

mathjax_path = \
    "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax" \
                ".js?config=TeX" \
              "-AMS-MML_HTMLorMML"


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'NEST simulator user documentation'
copyright = u'2004, nest-simulator'
author = u'nest-simulator'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'
# The full version, including alpha/beta/rc tagss
release = '1.0.0'
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'conngen',
    'nest_by_example', 'README.md']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# add numbered figure link
numfig = True

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NESTsimulatordoc'

html_show_sphinx = False
html_show_copyright = False

# This way works for ReadTheDocs
# With this local 'make html' is broken!
github_doc_root = ''

intersphinx_mapping = {'https://docs.python.org/': None}


#def skipUnwanted(app, what, name, obj, skip, options):
#    """Skip pynestkernel"""
#    if name == "pynestkernel":
#        return True
#    else:
#        return False

def setup(app):
    # app.add_stylesheet('css/my_styles.css')
    app.add_stylesheet('css/custom.css')
    app.add_javascript("js/custom.js")
    app.add_config_value('recommonmark_config', {
            'auto_toc_tree_section': 'Contents',
            'enable_inline_math': True,
            'enable_auto_doc_ref': True,
            'enable_eval_rst': True
            }, True)
    app.add_transform(AutoStructify)

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NESTsimulator.tex', u'NEST simulator Documentation',
     u'steffengraber', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nestsimulator', u'NEST simulator Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NESTsimulator', u'NEST simulator Documentation',
     author, 'NESTsimulator', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for readthedocs ----------------------------------------------
# on_rtd = os.environ.get('READTHEDOCS') == 'True'
# if on_rtd:
#    html_theme = 'alabaster'
# else:
#    html_theme = 'nat'

