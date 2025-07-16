#!/usr/bin/env python3
"""
Interactive parameter exploration demo for PDEVisualizer.

This script demonstrates the parameter exploration capabilities,
including parameter sweeps, comparisons, and sensitivity analysis.
"""

import numpy as np
import matplotlib.pyplot as plt
from pdevisualizer.parameter_exploration import ParameterExplorer, ParameterVisualizer
from pdevisualizer.solver import BoundaryCondition, InitialConditions


def demo_heat_diffusion_parameter_sweep():
    """Demonstrate parameter sweep for heat diffusion coefficient."""
    print("🔥 Heat Diffusion Parameter Sweep Demo")
    print("=" * 60)
    
    # Create explorer
    explorer = ParameterExplorer('heat', grid_shape=(50, 50))
    
    # Create initial condition - hot spots with different temperatures
    u0 = InitialConditions.multiple_sources(
        (50, 50),
        [(15, 15, 100.0), (35, 35, 80.0), (25, 10, 60.0)]
    )
    explorer.set_initial_conditions(u0)
    
    # Run parameter sweep for thermal diffusivity
    print("Running parameter sweep for thermal diffusivity (α)...")
    alpha_values = np.linspace(0.1, 0.8, 8)
    sweep_result = explorer.parameter_sweep('alpha', alpha_values, 
                                          custom_params={'steps': 150})
    
    # Plot results
    print("Creating visualizations...")
    fig1 = ParameterVisualizer.plot_parameter_sweep(sweep_result, figsize=(14, 10))
    fig1.savefig('heat_alpha_sweep_metrics.png', dpi=300, bbox_inches='tight')
    print("  Saved: heat_alpha_sweep_metrics.png")
    
    # Show solution comparison for selected values
    selected_indices = [0, 3, 7]  # Low, medium, high alpha
    selected_solutions = {
        f'α = {alpha_values[i]:.2f}': sweep_result.solutions[i] 
        for i in selected_indices
    }
    
    fig2 = ParameterVisualizer.plot_solution_comparison(selected_solutions, figsize=(15, 5))
    fig2.savefig('heat_alpha_comparison.png', dpi=300, bbox_inches='tight')
    print("  Saved: heat_alpha_comparison.png")
    
    # Analyze results
    max_temps = sweep_result.metrics['max_value']
    total_energies = sweep_result.metrics['total_energy']
    
    print(f"\nResults Analysis:")
    print(f"  α range: {alpha_values[0]:.2f} to {alpha_values[-1]:.2f}")
    print(f"  Max temperature range: {max_temps.min():.1f} to {max_temps.max():.1f}")
    print(f"  Total energy range: {total_energies.min():.1f} to {total_energies.max():.1f}")
    print(f"  Higher α leads to {'faster' if max_temps[-1] < max_temps[0] else 'slower'} diffusion")
    
    plt.close('all')  # Clean up
    print("✅ Heat diffusion parameter sweep completed!")


def demo_wave_propagation_parameter_grid():
    """Demonstrate parameter grid for wave propagation."""
    print("\n🌊 Wave Propagation Parameter Grid Demo")
    print("=" * 60)
    
    # Create explorer
    explorer = ParameterExplorer('wave', grid_shape=(40, 40))
    
    # Create initial condition - circular wave
    u0 = InitialConditions.circular_wave((40, 40), center=(20, 20), radius=8, amplitude=1.0)
    explorer.set_initial_conditions(u0)
    
    # Create parameter grid: wave speed vs time step
    print("Creating parameter grid for wave speed (c) vs time step (dt)...")
    c_values = np.array([0.5, 1.0, 1.5])
    dt_values = np.array([0.02, 0.05, 0.08])
    
    fig = ParameterVisualizer.plot_parameter_grid(
        explorer, 'c', c_values, 'dt', dt_values, 
        figsize=(12, 12), cmap='RdBu_r'
    )
    fig.savefig('wave_parameter_grid.png', dpi=300, bbox_inches='tight')
    print("  Saved: wave_parameter_grid.png")
    
    # Analyze stability
    print(f"\nParameter Grid Analysis:")
    print(f"  Wave speeds tested: {c_values}")
    print(f"  Time steps tested: {dt_values}")
    print(f"  Grid shows {len(c_values) * len(dt_values)} different parameter combinations")
    
    # Check CFL condition
    dx = dy = 1.0  # Grid spacing
    cfl_factors = np.outer(c_values, dt_values) * np.sqrt(1/dx**2 + 1/dy**2)
    print(f"  CFL factors range: {cfl_factors.min():.3f} to {cfl_factors.max():.3f}")
    print(f"  All combinations are {'stable' if cfl_factors.max() <= 1.0 else 'some unstable'}")
    
    plt.close('all')  # Clean up
    print("✅ Wave parameter grid completed!")


def demo_boundary_condition_comparison():
    """Demonstrate comparison of different boundary conditions."""
    print("\n🏠 Boundary Condition Comparison Demo")
    print("=" * 60)
    
    # Test different boundary conditions
    boundary_types = [
        ('Dirichlet (Cold)', BoundaryCondition.dirichlet(0.0)),
        ('Neumann (Insulated)', BoundaryCondition.neumann(0.0)),
        ('Periodic', BoundaryCondition.periodic())
    ]
    
    results = {}
    
    for name, boundary in boundary_types:
        print(f"Running simulation with {name} boundary...")
        
        explorer = ParameterExplorer('heat', grid_shape=(40, 40), boundary=boundary)
        
        # Hot spot in center
        u0 = InitialConditions.gaussian_pulse((40, 40), center=(20, 20), sigma=5, amplitude=100.0)
        explorer.set_initial_conditions(u0)
        
        # Run parameter sweep for diffusivity
        alpha_values = np.array([0.1, 0.3, 0.5])
        sweep_result = explorer.parameter_sweep('alpha', alpha_values, 
                                              custom_params={'steps': 100})
        
        # Store results for comparison
        results[name] = sweep_result
    
    # Create comparison plots
    print("Creating boundary condition comparison plots...")
    
    # Plot metrics comparison
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.ravel()
    
    metrics = ['max_value', 'min_value', 'total_energy', 'center_value']
    
    for i, metric in enumerate(metrics):
        ax = axes[i]
        
        for name, sweep_result in results.items():
            ax.plot(sweep_result.parameter_values, sweep_result.metrics[metric], 
                   'o-', label=name, linewidth=2, markersize=6)
        
        ax.set_xlabel('α (thermal diffusivity)')
        ax.set_ylabel(metric.replace('_', ' ').title())
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_title(f'{metric.replace("_", " ").title()} vs α')
    
    plt.tight_layout()
    plt.suptitle('Boundary Condition Effects on Heat Diffusion', fontsize=16, y=1.02)
    plt.savefig('boundary_condition_comparison.png', dpi=300, bbox_inches='tight')
    print("  Saved: boundary_condition_comparison.png")
    
    # Analyze differences
    print(f"\nBoundary Condition Analysis:")
    for name, sweep_result in results.items():
        final_energy = sweep_result.metrics['total_energy'][-1]  # High alpha case
        print(f"  {name}: Final energy = {final_energy:.1f}")
    
    plt.close('all')  # Clean up
    print("✅ Boundary condition comparison completed!")


def demo_sensitivity_analysis():
    """Demonstrate sensitivity analysis for parameter uncertainty."""
    print("\n📊 Sensitivity Analysis Demo")
    print("=" * 60)
    
    # Create explorer for wave equation
    explorer = ParameterExplorer('wave', grid_shape=(30, 30))
    
    # Create initial condition
    u0 = InitialConditions.sine_wave((30, 30), wavelength=10, amplitude=1.0, direction='diagonal')
    explorer.set_initial_conditions(u0)
    
    # Run sensitivity analysis for wave speed
    print("Running sensitivity analysis for wave speed...")
    base_c = 1.0
    sensitivity_result = explorer.sensitivity_analysis('c', base_c, 
                                                     perturbation_percent=25.0,
                                                     n_samples=7)
    
    # Plot sensitivity results
    fig = ParameterVisualizer.plot_sensitivity_analysis(sensitivity_result, figsize=(14, 6))
    fig.savefig('wave_sensitivity_analysis.png', dpi=300, bbox_inches='tight')
    print("  Saved: wave_sensitivity_analysis.png")
    
    # Analyze sensitivity
    sensitivity_metrics = sensitivity_result['sensitivity_metrics']
    print(f"\nSensitivity Analysis Results:")
    print(f"  Base wave speed: {base_c}")
    print(f"  Perturbation: ±{sensitivity_result['perturbation_percent']}%")
    print(f"  Parameter range tested: {sensitivity_result['parameter_values'].min():.3f} to {sensitivity_result['parameter_values'].max():.3f}")
    
    print(f"\nSensitivity Coefficients:")
    for metric, sensitivity in sensitivity_metrics.items():
        interpretation = "High" if sensitivity > 0.5 else "Medium" if sensitivity > 0.1 else "Low"
        print(f"  {metric}: {sensitivity:.3f} ({interpretation} sensitivity)")
    
    # Find most sensitive metric
    if sensitivity_metrics:
        most_sensitive = max(sensitivity_metrics.items(), key=lambda x: x[1])
        print(f"\nMost sensitive metric: {most_sensitive[0]} (coefficient: {most_sensitive[1]:.3f})")
    
    plt.close('all')  # Clean up
    print("✅ Sensitivity analysis completed!")


def demo_multi_parameter_exploration():
    """Demonstrate exploration of multiple parameters simultaneously."""
    print("\n🎯 Multi-Parameter Exploration Demo")
    print("=" * 60)
    
    # Create explorer
    explorer = ParameterExplorer('heat', grid_shape=(25, 25))
    
    # Create complex initial condition
    u0 = InitialConditions.multiple_sources(
        (25, 25),
        [(6, 6, 80.0), (19, 19, 60.0), (12, 6, 40.0), (6, 19, 20.0)]
    )
    explorer.set_initial_conditions(u0)
    
    # Define multiple parameter configurations
    print("Comparing multiple parameter configurations...")
    
    configs = [
        {'alpha': 0.1, 'dt': 0.1, 'steps': 100},    # Slow diffusion
        {'alpha': 0.3, 'dt': 0.1, 'steps': 100},    # Medium diffusion
        {'alpha': 0.5, 'dt': 0.05, 'steps': 200},   # Fast diffusion, fine time step
        {'alpha': 0.2, 'dt': 0.15, 'steps': 67},    # Coarse time step
        {'alpha': 0.4, 'dt': 0.08, 'steps': 125}    # Custom configuration
    ]
    
    labels = [
        'Slow (α=0.1)',
        'Medium (α=0.3)', 
        'Fast + Fine dt',
        'Coarse dt',
        'Custom'
    ]
    
    # Run comparison
    comparison_results = explorer.compare_parameters(configs, labels)
    
    # Plot comparison
    fig = ParameterVisualizer.plot_solution_comparison(comparison_results, 
                                                     figsize=(20, 4), 
                                                     cmap='plasma')
    fig.savefig('multi_parameter_comparison.png', dpi=300, bbox_inches='tight')
    print("  Saved: multi_parameter_comparison.png")
    
    # Analyze results
    print(f"\nMulti-Parameter Analysis:")
    for i, (label, solution) in enumerate(comparison_results.items()):
        config = configs[i]
        max_temp = np.max(solution)
        total_energy = np.sum(solution**2)
        
        print(f"  {label}:")
        print(f"    Config: α={config['alpha']}, dt={config['dt']}, steps={config['steps']}")
        print(f"    Max temp: {max_temp:.1f}, Total energy: {total_energy:.1f}")
    
    plt.close('all')  # Clean up
    print("✅ Multi-parameter exploration completed!")


def main():
    """Run all parameter exploration demonstrations."""
    print("🚀 PDEVisualizer Parameter Exploration Demo")
    print("=" * 80)
    print("This demo showcases advanced parameter exploration capabilities")
    print("for systematic analysis of PDE behavior under different conditions.")
    print("=" * 80)
    print()
    
    try:
        # Run all demonstrations
        demo_heat_diffusion_parameter_sweep()
        demo_wave_propagation_parameter_grid()
        demo_boundary_condition_comparison()
        demo_sensitivity_analysis()
        demo_multi_parameter_exploration()
        
        print("\n🎉 All parameter exploration demos completed successfully!")
        print("\nGenerated visualizations:")
        print("  - heat_alpha_sweep_metrics.png (parameter sweep metrics)")
        print("  - heat_alpha_comparison.png (solution comparison)")
        print("  - wave_parameter_grid.png (2D parameter grid)")
        print("  - boundary_condition_comparison.png (boundary effects)")
        print("  - wave_sensitivity_analysis.png (sensitivity analysis)")
        print("  - multi_parameter_comparison.png (multi-parameter study)")
        
        print("\nParameter exploration capabilities demonstrated:")
        print("  ✅ Parameter sweeps (1D parameter variation)")
        print("  ✅ Parameter grids (2D parameter space)")
        print("  ✅ Boundary condition effects")
        print("  ✅ Sensitivity analysis")
        print("  ✅ Multi-parameter comparisons")
        print("  ✅ Comprehensive visualization tools")
        
        print("\nThese tools enable:")
        print("  • Systematic parameter optimization")
        print("  • Understanding parameter sensitivity")
        print("  • Comparing different configurations")
        print("  • Analyzing boundary condition effects")
        print("  • Creating publication-quality plots")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        raise


if __name__ == "__main__":
    main()