# PDEVisualizer

[![PyPI version](https://badge.fury.io/py/pdevisualizer.svg)](https://badge.fury.io/py/pdevisualizer)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation Status](https://readthedocs.org/projects/pdevisualizer/badge/?version=latest)](https://pdevisualizer.readthedocs.io/en/latest/?badge=latest)
[![Tests](https://github.com/AdityaAnoop3/pdevisualizer/workflows/Tests/badge.svg)](https://github.com/AdityaAnoop3/pdevisualizer/actions)

A **lightweight, high-performance Python library** for prototyping and visualizing partial differential equations (PDEs). Built for researchers, educators, and students who need fast, beautiful PDE simulations without the complexity of full-scale finite element frameworks.

---

## ✨ Features

### 🔥 **Unified PDE Solver**
- ✅ **Heat equation** (diffusion, thermal dynamics)
- ✅ **Wave equation** (acoustic/seismic propagation)
- ✅ Clean, unified API for all equation types
- ✅ Numba-accelerated finite difference methods

### 🎨 **Advanced Visualization**
- ✅ Animated GIF/MP4 exports with matplotlib
- ✅ Contour plots and multi-panel comparisons
- ✅ Solution evolution tracking over time
- ✅ Publication-quality figures

### 🧪 **Boundary Conditions**
- ✅ **Dirichlet** (fixed values)
- ✅ **Neumann** (flux/gradient, insulated boundaries)
- ✅ **Periodic** (wraparound)

### 📊 **Parameter Exploration Tools**
- ✅ Parameter sweeps (single parameter analysis)
- ✅ Parameter grids (2D parameter space exploration)
- ✅ Sensitivity analysis
- ✅ Automated metrics tracking (max/min values, energy)
- ✅ Professional visualization of parameter effects

### 🚀 **Performance & Quality**
- ✅ Numba JIT compilation for computational hotspots
- ✅ 82% test coverage with 142 comprehensive tests
- ✅ CI/CD pipeline with GitHub Actions
- ✅ Type hints and professional code structure

---

## 🚀 Quick Start

### Installation

```bash
pip install pdevisualizer
```

### Basic Heat Equation

```python
import numpy as np
from pdevisualizer import PDESolver, InitialConditions, BoundaryCondition

# Create solver for heat equation on 50x50 grid
solver = PDESolver('heat', grid_shape=(50, 50))

# Set Gaussian initial temperature distribution
u0 = InitialConditions.gaussian_pulse((50, 50), center=(25, 25), sigma=5, amplitude=100)
solver.set_initial_conditions(u0)

# Configure parameters
solver.set_parameters(alpha=0.5, dt=0.1)

# Set boundary conditions (fixed temperature at edges)
solver.set_boundary_conditions(BoundaryCondition.dirichlet(0.0))

# Solve and get final state
solution = solver.solve(steps=200)

# Create animation
animation = solver.animate(steps=5, frames=100, interval=50)
animation.save('heat_diffusion.gif', writer='pillow')
```

### Wave Equation Example

```python
# 2D wave propagation (e.g., water ripples)
wave_solver = PDESolver('wave', grid_shape=(100, 100))

# Circular wave source at center
u0 = InitialConditions.circular_wave((100, 100), center=(50, 50), radius=10, amplitude=50)
wave_solver.set_initial_conditions(u0)

# Set wave speed and time step
wave_solver.set_parameters(c=1.0, dt=0.01)

# Periodic boundaries (wraparound edges)
wave_solver.set_boundary_conditions(BoundaryCondition.periodic())

# Simulate wave propagation
solution = wave_solver.solve(steps=500)
```

### Parameter Exploration

```python
from pdevisualizer.parameter_exploration import ParameterExplorer

# Explore how thermal diffusivity affects heat dissipation
explorer = ParameterExplorer('heat', grid_shape=(50, 50))
explorer.set_initial_conditions(u0)

# Sweep alpha from 0.1 to 1.0
alpha_values = np.linspace(0.1, 1.0, 10)
results = explorer.parameter_sweep('alpha', alpha_values, custom_params={'steps': 200})

# Visualize results
from pdevisualizer.parameter_exploration import ParameterVisualizer

visualizer = ParameterVisualizer()
fig = visualizer.plot_parameter_sweep(results, metric='max_value')
plt.savefig('parameter_sweep.png', dpi=150, bbox_inches='tight')
```

---

## 📚 Documentation

Full documentation is available at: **[pdevisualizer.readthedocs.io](https://pdevisualizer.readthedocs.io)**

### Topics Covered:
- Installation and setup
- Complete API reference
- Tutorial notebooks
- Advanced usage examples
- Contributing guidelines

---

## 🎯 Use Cases

- **Research**: Rapid prototyping of PDE models
- **Education**: Interactive demonstrations of PDE concepts
- **Exploration**: Parameter sensitivity studies
- **Visualization**: Publication-quality animations and plots

---

## 🛠️ Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/AdityaAnoop3/pdevisualizer.git
cd pdevisualizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev,docs]"

# Run tests
pytest -v --cov=pdevisualizer
```

### Project Structure

```
pdevisualizer/
├── src/pdevisualizer/
│   ├── solver.py                    # Unified PDE solver API
│   ├── heat2d.py                    # Heat equation solver
│   ├── wave2d.py                    # Wave equation solver
│   ├── boundary_conditions.py       # Boundary condition implementations
│   ├── parameter_exploration.py     # Parameter exploration tools
│   └── enhanced_visualizations.py   # Advanced visualization tools
├── tests/                           # Comprehensive test suite (82% coverage)
├── docs/                            # Sphinx documentation
└── notebooks/                       # Example Jupyter notebooks
```

---

## 📊 Performance

- **Numba JIT compilation** for computational kernels
- Efficient finite difference implementations
- Optimized for 2D grids up to 500x500
- Typical solve time: <1 second for 100x100 grid, 100 steps

---

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Areas for Contribution:
- Additional PDE types (Schrödinger, Burgers, etc.)
- 3D domain support
- More boundary condition types
- Additional visualization tools
- Performance optimizations

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Built with:
- [NumPy](https://numpy.org/) - Array operations
- [Numba](https://numba.pydata.org/) - JIT compilation
- [Matplotlib](https://matplotlib.org/) - Visualization
- [SciPy](https://scipy.org/) - Scientific computing

---

## 📧 Contact

**Aditya Anoop Nair**
- Email: adityaanoop@live.in
- GitHub: [@AdityaAnoop3](https://github.com/AdityaAnoop3)
- PyPI: [pdevisualizer](https://pypi.org/project/pdevisualizer/)

---

## 🌟 Star History

If you find this project useful, please consider giving it a star on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=AdityaAnoop3/pdevisualizer&type=Date)](https://star-history.com/#AdityaAnoop3/pdevisualizer&Date)
