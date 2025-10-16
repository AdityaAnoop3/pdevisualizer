Installation
============

Requirements
------------

* Python 3.10 or higher
* NumPy >= 1.24.0
* Matplotlib >= 3.7.0
* Numba >= 0.57.0
* SciPy >= 1.10.0

Install from PyPI
-----------------

The easiest way to install PDEVisualizer is via pip:

.. code-block:: bash

   pip install pdevisualizer

Install from Source
-------------------

To install from source for development:

.. code-block:: bash

   git clone https://github.com/AdityaAnoop3/pdevisualizer.git
   cd pdevisualizer
   pip install -e ".[dev,docs]"

Verify Installation
-------------------

.. code-block:: python

   import pdevisualizer
   print(pdevisualizer.__version__)
