PDEVisualizer Documentation
===========================

.. image:: https://badge.fury.io/py/pdevisualizer.svg
   :target: https://badge.fury.io/py/pdevisualizer
   :alt: PyPI version

.. image:: https://img.shields.io/badge/python-3.10+-blue.svg
   :target: https://www.python.org/downloads/
   :alt: Python 3.10+

.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT

A **lightweight, high-performance Python library** for prototyping and visualizing partial differential equations (PDEs). Built for researchers, educators, and students who need fast, beautiful PDE simulations without the complexity of full-scale finite element frameworks.

Features
--------

Core Capabilities
~~~~~~~~~~~~~~~~~

* **Heat Equation Solver** - Diffusion and thermal dynamics simulations
* **Wave Equation Solver** - Acoustic and seismic wave propagation
* **Unified API** - Clean, consistent interface for all PDE types
* **Numba-Accelerated** - JIT-compiled kernels for high performance

Boundary Conditions
~~~~~~~~~~~~~~~~~~~

* **Dirichlet** - Fixed value boundaries
* **Neumann** - Fixed flux/gradient (insulated boundaries)
* **Periodic** - Wraparound boundaries

Visualization Tools
~~~~~~~~~~~~~~~~~~~

* **Animated Exports** - GIF/MP4 output with matplotlib
* **Contour Plots** - Beautiful contour visualizations
* **Multi-Panel Comparisons** - Side-by-side solution comparisons
* **Evolution Tracking** - Solution development over time

Parameter Exploration
~~~~~~~~~~~~~~~~~~~~~

* **Parameter Sweeps** - Single parameter analysis
* **Parameter Grids** - 2D parameter space exploration
* **Sensitivity Analysis** - Understanding parameter effects
* **Automated Metrics** - Max/min values, energy tracking
* **Professional Visualizations** - Publication-quality plots

Quick Start
-----------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   pip install pdevisualizer

Basic Heat Equation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   from pdevisualizer import PDESolver, InitialConditions, BoundaryCondition

   # Create solver for heat equation on 50x50 grid
   solver = PDESolver('heat', grid_shape=(50, 50))

   # Set Gaussian initial temperature distribution
   u0 = InitialConditions.gaussian_pulse(
       (50, 50), center=(25, 25), sigma=5, amplitude=100
   )
   solver.set_initial_conditions(u0)

   # Configure parameters
   solver.set_parameters(alpha=0.5, dt=0.1)

   # Set boundary conditions
   solver.set_boundary_conditions(BoundaryCondition.dirichlet(0.0))

   # Solve and create animation
   solution = solver.solve(steps=200)
   animation = solver.animate(steps=5, frames=100, interval=50)
   animation.save('heat_diffusion.gif', writer='pillow')

Wave Equation Example
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # 2D wave propagation
   wave_solver = PDESolver('wave', grid_shape=(100, 100))

   # Circular wave source
   u0 = InitialConditions.circular_wave(
       (100, 100), center=(50, 50), radius=10, amplitude=50
   )
   wave_solver.set_initial_conditions(u0)
   wave_solver.set_parameters(c=1.0, dt=0.01)
   wave_solver.set_boundary_conditions(BoundaryCondition.periodic())

   # Simulate
   solution = wave_solver.solve(steps=500)

Parameter Exploration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from pdevisualizer.parameter_exploration import ParameterExplorer

   # Explore thermal diffusivity effects
   explorer = ParameterExplorer('heat', grid_shape=(50, 50))
   explorer.set_initial_conditions(u0)

   # Sweep alpha from 0.1 to 1.0
   alpha_values = np.linspace(0.1, 1.0, 10)
   results = explorer.parameter_sweep(
       'alpha', alpha_values, custom_params={'steps': 200}
   )

   # Visualize results
   from pdevisualizer.parameter_exploration import ParameterVisualizer
   visualizer = ParameterVisualizer()
   fig = visualizer.plot_parameter_sweep(results, metric='max_value')

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   installation
   quickstart
   tutorials/index
   examples/index

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   api/solver
   api/boundary_conditions
   api/parameter_exploration
   api/enhanced_visualizations
   api/heat2d
   api/wave2d

.. toctree::
   :maxdepth: 1
   :caption: Development

   contributing
   changelog
   license

Performance
-----------

* **Numba JIT compilation** for computational kernels
* Efficient finite difference implementations
* Optimized for 2D grids up to 500x500
* Typical solve time: <1 second for 100x100 grid, 100 steps

Use Cases
---------

Research
~~~~~~~~
Rapid prototyping of PDE models for scientific investigations.

Education
~~~~~~~~~
Interactive demonstrations of PDE concepts for teaching.

Exploration
~~~~~~~~~~~
Parameter sensitivity studies and model optimization.

Visualization
~~~~~~~~~~~~~
Publication-quality animations and plots for papers and presentations.

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`