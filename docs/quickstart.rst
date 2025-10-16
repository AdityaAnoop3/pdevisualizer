Quick Start Guide
=================

This guide will help you get started with PDEVisualizer in just a few minutes.

Your First Heat Equation
-------------------------

.. code-block:: python

   import numpy as np
   from pdevisualizer import PDESolver, InitialConditions, BoundaryCondition

   # Create solver
   solver = PDESolver('heat', grid_shape=(50, 50))

   # Set initial conditions
   u0 = InitialConditions.gaussian_pulse(
       (50, 50), center=(25, 25), sigma=5, amplitude=100
   )
   solver.set_initial_conditions(u0)

   # Configure solver
   solver.set_parameters(alpha=0.5, dt=0.1)
   solver.set_boundary_conditions(BoundaryCondition.dirichlet(0.0))

   # Solve
   solution = solver.solve(steps=200)

   # Animate
   animation = solver.animate(steps=5, frames=100)
   animation.save('heat.gif', writer='pillow')

Wave Propagation
----------------

.. code-block:: python

   # Create wave solver
   wave_solver = PDESolver('wave', grid_shape=(100, 100))

   # Circular wave
   u0 = InitialConditions.circular_wave(
       (100, 100), center=(50, 50), radius=10
   )
   wave_solver.set_initial_conditions(u0)
   wave_solver.set_parameters(c=1.0, dt=0.01)
   wave_solver.set_boundary_conditions(BoundaryCondition.periodic())

   # Solve
   solution = wave_solver.solve(steps=500)

Parameter Exploration
---------------------

.. code-block:: python

   from pdevisualizer.parameter_exploration import ParameterExplorer

   explorer = ParameterExplorer('heat', grid_shape=(50, 50))
   explorer.set_initial_conditions(u0)

   alpha_values = np.linspace(0.1, 1.0, 10)
   results = explorer.parameter_sweep(
       'alpha', alpha_values, custom_params={'steps': 200}
   )

Next Steps
----------

* Explore the :doc:`API Reference <api/solver>`
* Check out complete :doc:`Examples <examples/index>`
* Read the :doc:`Tutorials <tutorials/index>`
