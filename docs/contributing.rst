Contributing
============

We welcome contributions! Here's how you can help:

Development Setup
-----------------

.. code-block:: bash

   git clone https://github.com/AdityaAnoop3/pdevisualizer.git
   cd pdevisualizer
   python -m venv venv
   source venv/bin/activate
   pip install -e ".[dev,docs]"

Running Tests
-------------

.. code-block:: bash

   pytest -v --cov=pdevisualizer

Code Style
----------

We use Black for formatting and Flake8 for linting:

.. code-block:: bash

   black src/ tests/
   flake8 src/ tests/

Areas for Contribution
----------------------

* Additional PDE types (Schrödinger, Burgers, etc.)
* 3D domain support
* More boundary condition types
* Additional visualization tools
* Performance optimizations
* Documentation improvements

Submitting Pull Requests
-------------------------

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run the test suite
6. Submit a pull request

Code of Conduct
---------------

Please be respectful and constructive in all interactions.
