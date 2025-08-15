Build documentation
===================

The documentation is built with `Sphinx <http://www.sphinx-doc.org>`_:

.. code-block:: bash

    python setup.py install                        # Install package
    pip install -r docs/requirements.txt           # Install requirements
    cd docs                                        # Change to docs folder
    make html                                      # Build documentation


The generated documentation is located in docs/_build/html.