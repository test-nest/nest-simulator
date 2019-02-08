Instructions for creating a PyNEST example script
=======================================================

.. admonition:: Important!

  If you want to contribute your example to the NEST project, make sure you follow our :ref:`Git workflow <git_workflow>`.

Format your python script
----------------------------

**Use our template**
~~~~~~~~~~~~~~~~~~~~~~

Copy the :doc:`pynest_examples_template.py <pynest_example>` and carefully read the instructions.

Replace the template text with appropriate text for your example.

**Rename your python script**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If your example contains a plot or other image as output
ensure that the name of the file begins with `plot_`

.. pull-quote::

   For example: ``plot_my_example.py``.

And ensure that the file is put in the ``pynest/examples`` folder.



If the output of your example is only text (e.g., `print(values)`), name your file
``my_example.py``

**Check that code is complete**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script must be executable; thus, you must include all necessary imports and
end your script with the command to show the output.

If there is a specific configuration or other requirement to make this script run, you
must explictly state this information in the initial docstring (:doc:`see template <pynest_example>`).

.. pull-quote::

   For example, "MUSIC needs to be installed and configured in NEST: ``cmake -Dwith-music=[ON</path/to/music>]``"


Test your python script
-------------------------

Make sure that your script can be executed in python/ipython with no errors, and that
the output appears correctly.


.. code-block:: bash

   ipython

.. code-block:: python

   %run ./plot_my_example.py

----

(Optional) Generate the documentation files for your script
-------------------------------------------------------------

We use `sphinx_gallery <https://sphinx-gallery.readthedocs.io/en/latest/>`_ for generating the PyNEST examples.
Along with generating HTML, this extension allows us to autogenerate a Jupyter Notebook file, python file, and images of the scripts in a gallery.

If you want to check if your script generates HTML properly with sphinx,
you can run a sphinx environment and build the output files locally.


Install the prerequisites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to have the following installed:

 * a :doc:`recent NEST build <../../../installation/index>`
 * `sphinx <https://www.sphinx-doc.org/en/master/index.html>`_
 * `sphinx_gallery <https://sphinx-gallery.readthedocs.io/en/latest/>`_
 * `Matplotlib <https://matplotlib.org/>`_ (sphinx_gallery dependency)
 * `Pillow <https://python-pillow.org/>`_   (sphinx_gallery dependency)
 * A number of other dependencies - depending on the requirements to run your script (e.g., NumPy).


Alternatively, you can follow the instructions for :ref:`creating a new conda environment <local_install_docs>`, which includes all the dependencies to run sphinx and a NEST build.


Configure files to run sphinx-gallery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To test your script and avoid having to run all other examples, we recommend the following workflow.

Create a directory to test your script in:

.. code-block:: bash

   mkdir sphinxtest_myexample/
   cd sphinxtest_myexample/

Run sphinx-quickstart.
You will be prompted to answer some set up questions on the command line.

.. code-block:: bash

   sphinx-quickstart

You can use most of the defaults by pressing enter after every question.

We recommend, however, that you say `yes` to mathjax and `no` to Create Windows command file:

.. code-block:: console

   mathjax: include math, rendered in the browser by MathJax (y/n) [n]: y
   Create Windows command file? (y/n) [y]: n

Sphinx will create a ``_build`` directory as well as the following files:

* ``./conf.py``
* ``./index.rst``
* ``./Makefile``

Now let's configure sphinx to include sphinx-gallery.

Open ``conf.py`` and add ``sphinx_gallery.gen_gallery`` to the extensions:

.. code-block:: python
   :lineno-start: 34

   extensions = ['sphinx.ext.mathjax',
                 'sphinx_gallery.gen_gallery']

Add a new section called ``sphinx_gallery_conf`` and include the correct paths:

.. code-block:: python
   :lineno-start: 38

   sphinx_gallery_conf = {
       #path to your example scripts
       'examples_dirs': 'examples/',
       #path where to save gallery generated examples
       'gallery_dirs': 'auto_examples',
   }

Save and close the ``conf.py``.



In ``conf.py``, we said our `examples_dirs` is ``examples/`` but we have not created this directory yet.

Make a directory called ``examples/`` and put your example script inside it.

.. code-block:: bash

   mkdir examples/
   mv path/to/plot_my_example.py examples/


In the ``examples/`` directory create a ``README.txt`` file that contains the following:

.. code-block:: rest
   :linenos:

   My gallery
   ===========

A README file is required in the ``examples/`` folder for sphinx-gallery to work.

Open the ``index.rst`` file and include auto_examples/index to the table of contents:

.. code-block:: rest
   :lineno-start: 9

   .. toctree::
      :maxdepth: 2
      :caption: Contents

      auto_examples/index


Save and close the ``index.rst`` file.

Now all necessary files should be configured correctly, and you can generate the HTML:

.. code-block:: bash

   make html

If it's successful, the ``_build`` directory will contain the HTML files and a ``auto_examples`` directory
will appear and contain the autogenerated rst files, images, Jupyter Notebook, and python files.

.. note::

  If the build fails because "nest module not found", your path variables may not be set correctly.
  This may also be the case if Python cannot load the nest module due to missing or incompatible libraries.
  In this case, please run

        ``source </path/to/nest_install_dir>/bin/nest_vars.sh``

View the HTML by running

.. code-block:: sh

   xdg-open _build/html/index.html


In your browser, you should see a generic `Welcome to project_name's documentation` page with a link to your gallery.

.. note::

   This webpage will NOT look like the NEST documentation website because we have not set up the same theme
   in your test case. NEST uses a modified version of the ``sphinx_rtd_theme``. To replace the theme go to https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html

Check the html version of your script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please make sure that

* the code is in code blocks
* comment blocks are outside code blocks
* all output is generated correctly (e.g., image appears, values are shown and are correct)
* references are properly formatted
* content is clear, and there are no grammar mistakes

Next steps
-----------

When you feel that your PyNEST script is ready for review, you can :ref:`make a pull reqest <pull_requests>`.
