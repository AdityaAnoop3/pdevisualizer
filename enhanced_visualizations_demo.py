#!/usr/bin/env python3
"""
Enhanced Visualizations Demo for PDEVisualizer
Demonstrates advanced 2D visualization capabilities that build upon
the existing matplotlib patterns in the codebase.
"""

import numpy as np
import matplotlib.pyplot as plt
from pdevisualizer.enhanced_visualizations import EnhancedVisualizer
from pdevisualizer.parameter_exploration import ParameterExplorer
from pdevisualizer.solver import InitialConditions, BoundaryCondition, PDESolver
import time


def demo_contour_plots():
    """Demonstrate contour plot capabilities."""
    print("🗺️  Demonstrating Contour Plots...")
    
    # Create a solution with multiple features using your existing patterns
    explorer = ParameterExplorer('heat', grid_shape=(40, 40))
    u0 = InitialConditions.multiple_sources(
        (40, 40), 
        [(10, 10, 100.0), (30, 30, 80.0), (20, 15, 60.0)]
    )
    explorer.set_initial_conditions(u0)
    
    # Solve to get an interesting solution
    solver = PDESolver('heat', grid_shape=(40, 40))
    solver.set_parameters(alpha=0.25, dt=0.1)
    solver.set_initial_conditions(u0)
    solution = solver.solve(steps=50)
    
    # Filled contours
    fig1 = EnhancedVisualizer.plot_contours(
        solution, 
        title="Heat Distribution - Filled Contours",
        fill_contours=True,
        levels=20,
        cmap='hot'
    )
    plt.savefig('contour_filled.png', dpi=150, bbox_inches='tight')
    plt.close(fig1)
    
    # Line contours
    fig2 = EnhancedVisualizer.plot_contours(
        solution, 
        title="Heat Distribution - Line Contours",
        fill_contours=False,
        levels=15,
        cmap='hot'
    )
    plt.savefig('contour_lines.png', dpi=150, bbox_inches='tight')
    plt.close(fig2)
    
    print("  ✅ Contour plots saved")


def demo_solution_evolution():
    """Demonstrate solution evolution visualization."""
    print("⏳ Demonstrating Solution Evolution...")
    
    # Create heat equation evolution
    explorer = ParameterExplorer('heat', grid_shape=(30, 30))
    u0 = InitialConditions.gaussian_pulse((30, 30), center=(15, 15), sigma=5)
    explorer.set_initial_conditions(u0)
    
    # Generate solutions at different time points
    time_points = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    solutions = []
    
    for t in time_points:
        if t == 0.0:
            solutions.append(u0)
        else:
            steps = int(t * 100)  # 100 steps per time unit
            solver = PDESolver('heat', grid_shape=(30, 30))
            solver.set_parameters(alpha=0.25, dt=0.01)
            solver.set_initial_conditions(u0)
            solution = solver.solve(steps=steps)
            solutions.append(solution)
    
    # Create evolution plots with different visualization types
    fig1 = EnhancedVisualizer.plot_solution_evolution(
        solutions, 
        time_points, 
        title="Heat Diffusion Evolution (Heatmap)",
        plot_type='heatmap',
        cmap='hot',
        figsize=(18, 12)
    )
    plt.savefig('evolution_heatmap.png', dpi=150, bbox_inches='tight')
    plt.close(fig1)
    
    fig2 = EnhancedVisualizer.plot_solution_evolution(
        solutions, 
        time_points, 
        title="Heat Diffusion Evolution (Contour)",
        plot_type='contour',
        cmap='hot',
        figsize=(18, 12)
    )
    plt.savefig('evolution_contour.png', dpi=150, bbox_inches='tight')
    plt.close(fig2)
    
    print("  ✅ Solution evolution plots saved")


def demo_parameter_landscape():
    """Demonstrate parameter landscape visualization."""
    print("🗻 Demonstrating Parameter Landscape...")
    
    # Create explorer for parameter landscape
    explorer = ParameterExplorer('heat', grid_shape=(20, 20))
    u0 = InitialConditions.gaussian_pulse((20, 20), center=(10, 10), sigma=4)
    explorer.set_initial_conditions(u0)
    
    # Create parameter landscape (small resolution for demo speed)
    fig = EnhancedVisualizer.plot_parameter_landscape(
        explorer,
        'alpha', (0.1, 0.5),
        'dt', (0.05, 0.15),
        metric='max_value',
        resolution=8,  # Small for demo speed
        figsize=(12, 9)
    )
    plt.savefig('parameter_landscape.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print("  ✅ Parameter landscape saved")


def demo_enhanced_comparisons():
    """Demonstrate enhanced solution comparison capabilities."""
    print("🔍 Demonstrating Enhanced Solution Comparisons...")
    
    # Create solutions with different boundary conditions
    boundary_conditions = [
        ('Dirichlet', BoundaryCondition.dirichlet(0.0)),
        ('Neumann', BoundaryCondition.neumann(0.0)),
        ('Periodic', BoundaryCondition.periodic())
    ]
    
    solutions = {}
    
    for name, boundary in boundary_conditions:
        explorer = ParameterExplorer('heat', grid_shape=(20, 20), boundary=boundary)
        u0 = InitialConditions.gaussian_pulse((20, 20), center=(10, 10), sigma=3)
        explorer.set_initial_conditions(u0)
        
        # Solve with identical parameters
        solver = PDESolver('heat', grid_shape=(20, 20), boundary=boundary)
        solver.set_parameters(alpha=0.25, dt=0.1)
        solver.set_initial_conditions(u0)
        solution = solver.solve(steps=100)
        
        solutions[f'{name} BC'] = solution
    
    # Create enhanced comparison with multiple plot types
    fig = EnhancedVisualizer.plot_solution_comparison_enhanced(
        solutions,
        plot_types=['heatmap', 'contour'],
        figsize=(15, 10),
        cmap='hot'
    )
    plt.savefig('enhanced_comparison.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print("  ✅ Enhanced comparison saved")


def demo_enhanced_parameter_sweep():
    """Demonstrate enhanced parameter sweep visualization."""
    print("📊 Demonstrating Enhanced Parameter Sweep...")
    
    # Create explorer
    explorer = ParameterExplorer('wave', grid_shape=(25, 25))
    u0 = InitialConditions.gaussian_pulse((25, 25), center=(12, 12), sigma=4)
    explorer.set_initial_conditions(u0)
    
    # Run parameter sweep
    c_values = np.linspace(0.5, 2.0, 4)
    sweep_result = explorer.parameter_sweep('c', c_values, 
                                           custom_params={'steps': 150})
    
    # Create enhanced parameter sweep visualization
    fig = EnhancedVisualizer.plot_parameter_sweep_enhanced(
        sweep_result,
        include_heatmaps=True,
        include_contours=True,
        figsize=(16, 12)
    )
    plt.savefig('enhanced_parameter_sweep.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print("  ✅ Enhanced parameter sweep saved")


def demo_equation_specific_comparisons():
    """Demonstrate equation-specific visualization optimizations."""
    print("🔥 Demonstrating Equation-Specific Visualizations...")
    
    # Heat equation comparison
    heat_solutions = {}
    for alpha in [0.1, 0.3, 0.5]:
        explorer = ParameterExplorer('heat', grid_shape=(25, 25))
        u0 = InitialConditions.gaussian_pulse((25, 25), center=(12, 12), sigma=4)
        explorer.set_initial_conditions(u0)
        
        solver = PDESolver('heat', grid_shape=(25, 25))
        solver.set_parameters(alpha=alpha, dt=0.1)
        solver.set_initial_conditions(u0)
        solution = solver.solve(steps=100)
        
        heat_solutions[f'α = {alpha}'] = solution
    
    # Heat-optimized comparison
    fig1 = EnhancedVisualizer.plot_heat_comparison(
        heat_solutions,
        figsize=(15, 5)
    )
    plt.savefig('heat_comparison.png', dpi=150, bbox_inches='tight')
    plt.close(fig1)
    
    # Wave equation comparison
    wave_solutions = {}
    for c in [0.5, 1.0, 1.5]:
        explorer = ParameterExplorer('wave', grid_shape=(25, 25))
        u0 = InitialConditions.gaussian_pulse((25, 25), center=(12, 12), sigma=4)
        explorer.set_initial_conditions(u0)
        
        solver = PDESolver('wave', grid_shape=(25, 25))
        solver.set_parameters(c=c, dt=0.05)
        solver.set_initial_conditions(u0)
        solution = solver.solve(steps=200)
        
        wave_solutions[f'c = {c}'] = solution
    
    # Wave-optimized comparison
    fig2 = EnhancedVisualizer.plot_wave_comparison(
        wave_solutions,
        figsize=(15, 5),
        symmetric_colormap=True
    )
    plt.savefig('wave_comparison.png', dpi=150, bbox_inches='tight')
    plt.close(fig2)
    
    print("  ✅ Equation-specific comparisons saved")


def demo_multi_scale_visualization():
    """Demonstrate multi-scale visualization capabilities."""
    print("🔬 Demonstrating Multi-Scale Visualizations...")
    
    # Create a solution with multiple scales
    explorer = ParameterExplorer('heat', grid_shape=(50, 50))
    
    # Multiple heat sources at different scales
    u0 = InitialConditions.multiple_sources(
        (50, 50), 
        [(10, 10, 100.0), (40, 40, 80.0), (25, 25, 120.0), (15, 35, 60.0)]
    )
    explorer.set_initial_conditions(u0)
    
    # Solve at different time scales
    time_scales = [10, 50, 100, 200]
    solutions = {}
    
    for steps in time_scales:
        solver = PDESolver('heat', grid_shape=(50, 50))
        solver.set_parameters(alpha=0.25, dt=0.1)
        solver.set_initial_conditions(u0)
        solution = solver.solve(steps=steps)
        solutions[f'{steps} steps'] = solution
    
    # Create multi-scale comparison
    fig1 = EnhancedVisualizer.plot_heat_comparison(
        solutions,
        figsize=(20, 5)
    )
    plt.savefig('multi_scale_heatmap.png', dpi=150, bbox_inches='tight')
    plt.close(fig1)
    
    # Also create contour version
    fig2 = EnhancedVisualizer.plot_solution_comparison_enhanced(
        solutions,
        plot_types=['contour'],
        figsize=(20, 5),
        cmap='hot'
    )
    plt.savefig('multi_scale_contour.png', dpi=150, bbox_inches='tight')
    plt.close(fig2)
    
    print("  ✅ Multi-scale visualizations saved")


def main():
    """Run the complete enhanced visualizations demo."""
    print("🚀 Starting Enhanced Visualizations Demo")
    print("=" * 60)
    
    start_time = time.time()
    
    try:
        # Run all demonstrations
        demo_contour_plots()
        print()
        
        demo_solution_evolution()
        print()
        
        demo_parameter_landscape()
        print()
        
        demo_enhanced_comparisons()
        print()
        
        demo_enhanced_parameter_sweep()
        print()
        
        demo_equation_specific_comparisons()
        print()
        
        demo_multi_scale_visualization()
        print()
        
        # Summary
        total_time = time.time() - start_time
        print("=" * 60)
        print("🎉 Enhanced Visualizations Demo Results:")
        print(f"   ✅ Contour plots: CREATED")
        print(f"   ✅ Solution evolution: CREATED")
        print(f"   ✅ Parameter landscape: CREATED")
        print(f"   ✅ Enhanced comparisons: CREATED")
        print(f"   ✅ Enhanced parameter sweep: CREATED")
        print(f"   ✅ Equation-specific comparisons: CREATED")
        print(f"   ✅ Multi-scale visualizations: CREATED")
        print(f"   ⏱️  Total execution time: {total_time:.2f} seconds")
        print()
        print("🎯 Generated Files:")
        print("   📈 contour_filled.png")
        print("   📈 contour_lines.png")
        print("   📈 evolution_heatmap.png")
        print("   📈 evolution_contour.png")
        print("   📈 parameter_landscape.png")
        print("   📈 enhanced_comparison.png")
        print("   📈 enhanced_parameter_sweep.png")
        print("   📈 heat_comparison.png")
        print("   📈 wave_comparison.png")
        print("   📈 multi_scale_heatmap.png")
        print("   📈 multi_scale_contour.png")
        print()
        print("✨ Enhanced 2D Visualizations Module: FULLY FUNCTIONAL!")
        print("🎨 Ready for professional scientific visualizations!")
        
        return True
        
    except Exception as e:
        print(f"❌ Enhanced visualizations demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)