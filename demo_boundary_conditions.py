#!/usr/bin/env python3
"""
Demo script showcasing flexible boundary conditions in PDEVisualizer.

This script demonstrates the different types of boundary conditions
and their effects on heat diffusion and wave propagation.
"""

import numpy as np
import matplotlib.pyplot as plt
from pdevisualizer import PDESolver, BoundaryCondition, InitialConditions


def demo_heat_boundary_comparison():
    """Compare different boundary conditions for heat equation."""
    print("🔥 Heat Equation Boundary Comparison")
    print("=" * 50)
    
    # Common setup
    grid_shape = (50, 50)
    
    # Hot spot in center
    u0 = InitialConditions.zeros(grid_shape)
    u0[25, 25] = 100.0
    
    # Test different boundary conditions
    boundary_types = [
        ("Dirichlet (Cold)", BoundaryCondition.dirichlet(0.0)),
        ("Dirichlet (Hot)", BoundaryCondition.dirichlet(50.0)),
        ("Neumann (Insulated)", BoundaryCondition.neumann(0.0)),
        ("Periodic", BoundaryCondition.periodic())
    ]
    
    results = {}
    
    for name, boundary in boundary_types:
        print(f"\nTesting {name} boundary...")
        
        solver = PDESolver('heat', grid_shape=grid_shape, boundary=boundary)
        solver.set_parameters(alpha=0.25, dt=0.1)
        solver.set_initial_conditions(u0)
        
        # Solve
        result = solver.solve(steps=100)
        results[name] = result
        
        # Print statistics
        total_heat = np.sum(result)
        max_temp = np.max(result)
        min_temp = np.min(result)
        
        print(f"  Total heat: {total_heat:.1f}")
        print(f"  Max temperature: {max_temp:.1f}")
        print(f"  Min temperature: {min_temp:.1f}")
        print(f"  Heat conservation: {total_heat/100.0:.3f}")
        
        # Create animation
        anim = solver.animate(frames=150, interval=50)
        filename = f"heat_{name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.gif"
        anim.save(filename, writer="pillow")
        print(f"  Saved: {filename}")
    
    print("\n✅ Heat boundary comparison complete!")
    return results


def demo_wave_boundary_comparison():
    """Compare different boundary conditions for wave equation."""
    print("\n🌊 Wave Equation Boundary Comparison")
    print("=" * 50)
    
    # Common setup
    grid_shape = (60, 60)
    
    # Gaussian pulse in center
    u0 = InitialConditions.gaussian_pulse(grid_shape, center=(30, 30), sigma=5, amplitude=2.0)
    
    # Test different boundary conditions
    boundary_types = [
        ("Dirichlet (Fixed)", BoundaryCondition.dirichlet(0.0)),
        ("Neumann (Reflecting)", BoundaryCondition.neumann(0.0)),
        ("Periodic", BoundaryCondition.periodic()),
        ("Absorbing", BoundaryCondition.absorbing())
    ]
    
    results = {}
    
    for name, boundary in boundary_types:
        print(f"\nTesting {name} boundary...")
        
        solver = PDESolver('wave', grid_shape=grid_shape, boundary=boundary)
        solver.set_parameters(c=1.0, dt=0.05)
        solver.set_initial_conditions(u0)
        
        # Solve for longer time to see boundary effects
        result = solver.solve(steps=200)
        results[name] = result
        
        # Print statistics
        total_energy = np.sum(result**2)
        max_amplitude = np.max(np.abs(result))
        boundary_energy = (np.sum(result[0, :]**2) + np.sum(result[-1, :]**2) + 
                          np.sum(result[:, 0]**2) + np.sum(result[:, -1]**2))
        
        print(f"  Total energy: {total_energy:.3f}")
        print(f"  Max amplitude: {max_amplitude:.3f}")
        print(f"  Boundary energy: {boundary_energy:.3f}")
        
        # Create animation
        anim = solver.animate(frames=200, interval=50)
        filename = f"wave_{name.lower().replace(' ', '_').replace('(', '').replace(')', '')}.gif"
        anim.save(filename, writer="pillow")
        print(f"  Saved: {filename}")
    
    print("\n✅ Wave boundary comparison complete!")
    return results


def demo_insulated_vs_conducting():
    """Demonstrate insulated vs conducting boundaries."""
    print("\n🏠 Insulated vs Conducting Boundaries")
    print("=" * 50)
    
    grid_shape = (40, 40)
    
    # Hot spot in corner (to see boundary effects clearly)
    u0 = InitialConditions.zeros(grid_shape)
    u0[10, 10] = 100.0
    
    # Insulated boundaries (Neumann)
    print("\nInsulated boundaries (no heat loss)...")
    solver_insulated = PDESolver('heat', grid_shape=grid_shape, 
                                boundary=BoundaryCondition.neumann(0.0))
    solver_insulated.set_parameters(alpha=0.2, dt=0.1)
    solver_insulated.set_initial_conditions(u0)
    result_insulated = solver_insulated.solve(steps=100)
    
    # Conducting boundaries (Dirichlet)
    print("Conducting boundaries (heat loss to environment)...")
    solver_conducting = PDESolver('heat', grid_shape=grid_shape,
                                 boundary=BoundaryCondition.dirichlet(0.0))
    solver_conducting.set_parameters(alpha=0.2, dt=0.1)
    solver_conducting.set_initial_conditions(u0)
    result_conducting = solver_conducting.solve(steps=100)
    
    # Compare heat conservation
    heat_insulated = np.sum(result_insulated)
    heat_conducting = np.sum(result_conducting)
    
    print(f"Heat remaining (insulated): {heat_insulated:.1f} (conservation: {heat_insulated/100:.3f})")
    print(f"Heat remaining (conducting): {heat_conducting:.1f} (conservation: {heat_conducting/100:.3f})")
    print(f"Heat loss due to boundaries: {100 - heat_conducting:.1f}")
    
    # Create animations
    anim_insulated = solver_insulated.animate(frames=150, interval=50)
    anim_insulated.save("heat_insulated.gif", writer="pillow")
    
    anim_conducting = solver_conducting.animate(frames=150, interval=50)
    anim_conducting.save("heat_conducting.gif", writer="pillow")
    
    print("Saved: heat_insulated.gif, heat_conducting.gif")
    print("✅ Insulation comparison complete!")


def demo_wave_reflections():
    """Demonstrate wave reflections vs absorption."""
    print("\n🏓 Wave Reflections vs Absorption")
    print("=" * 50)
    
    grid_shape = (50, 50)
    
    # Pulse starting near left edge
    u0 = InitialConditions.gaussian_pulse(grid_shape, center=(15, 25), sigma=3, amplitude=1.0)
    
    # Reflecting boundaries (Neumann)
    print("\nReflecting boundaries...")
    solver_reflecting = PDESolver('wave', grid_shape=grid_shape,
                                 boundary=BoundaryCondition.neumann(0.0))
    solver_reflecting.set_parameters(c=1.0, dt=0.05)
    solver_reflecting.set_initial_conditions(u0)
    result_reflecting = solver_reflecting.solve(steps=150)
    
    # Absorbing boundaries
    print("Absorbing boundaries...")
    solver_absorbing = PDESolver('wave', grid_shape=grid_shape,
                                boundary=BoundaryCondition.absorbing())
    solver_absorbing.set_parameters(c=1.0, dt=0.05)
    solver_absorbing.set_initial_conditions(u0)
    result_absorbing = solver_absorbing.solve(steps=150)
    
    # Compare energy retention
    energy_reflecting = np.sum(result_reflecting**2)
    energy_absorbing = np.sum(result_absorbing**2)
    
    print(f"Energy (reflecting): {energy_reflecting:.3f}")
    print(f"Energy (absorbing): {energy_absorbing:.3f}")
    print(f"Energy absorption: {1 - energy_absorbing/energy_reflecting:.3f}")
    
    # Create animations
    anim_reflecting = solver_reflecting.animate(frames=200, interval=50)
    anim_reflecting.save("wave_reflecting.gif", writer="pillow")
    
    anim_absorbing = solver_absorbing.animate(frames=200, interval=50)
    anim_absorbing.save("wave_absorbing.gif", writer="pillow")
    
    print("Saved: wave_reflecting.gif, wave_absorbing.gif")
    print("✅ Wave reflection comparison complete!")


def demo_periodic_boundaries():
    """Demonstrate periodic boundary conditions."""
    print("\n🔄 Periodic Boundary Conditions")
    print("=" * 50)
    
    grid_shape = (40, 40)
    
    # Asymmetric initial condition (to see periodic effects)
    u0 = InitialConditions.zeros(grid_shape)
    u0[10:15, 10:15] = 50.0  # Square hot region
    
    # Heat equation with periodic boundaries
    print("Heat diffusion with periodic boundaries...")
    solver_heat = PDESolver('heat', grid_shape=grid_shape,
                           boundary=BoundaryCondition.periodic())
    solver_heat.set_parameters(alpha=0.15, dt=0.1)
    solver_heat.set_initial_conditions(u0)
    result_heat = solver_heat.solve(steps=200)
    
    # Wave equation with periodic boundaries
    print("Wave propagation with periodic boundaries...")
    u0_wave = InitialConditions.gaussian_pulse(grid_shape, center=(10, 20), sigma=3, amplitude=1.0)
    solver_wave = PDESolver('wave', grid_shape=grid_shape,
                           boundary=BoundaryCondition.periodic())
    solver_wave.set_parameters(c=1.0, dt=0.05)
    solver_wave.set_initial_conditions(u0_wave)
    result_wave = solver_wave.solve(steps=150)
    
    print(f"Heat conservation: {np.sum(result_heat)/np.sum(u0):.3f}")
    print(f"Wave energy: {np.sum(result_wave**2):.3f}")
    
    # Create animations
    anim_heat = solver_heat.animate(frames=250, interval=50)
    anim_heat.save("heat_periodic.gif", writer="pillow")
    
    anim_wave = solver_wave.animate(frames=200, interval=50)
    anim_wave.save("wave_periodic.gif", writer="pillow")
    
    print("Saved: heat_periodic.gif, wave_periodic.gif")
    print("✅ Periodic boundary demonstration complete!")


def main():
    """Run all boundary condition demonstrations."""
    print("🚀 PDEVisualizer Boundary Conditions Demo")
    print("=" * 60)
    print("This demo showcases different boundary condition types")
    print("and their effects on heat diffusion and wave propagation.")
    print("=" * 60)
    print()
    
    try:
        # Run all demonstrations
        demo_heat_boundary_comparison()
        demo_wave_boundary_comparison()
        demo_insulated_vs_conducting()
        demo_wave_reflections()
        demo_periodic_boundaries()
        
        print("\n🎉 All boundary condition demos completed successfully!")
        print("\nGenerated animations:")
        print("  Heat equation:")
        print("    - heat_dirichlet_cold.gif")
        print("    - heat_dirichlet_hot.gif")
        print("    - heat_neumann_insulated.gif")
        print("    - heat_periodic.gif")
        print("    - heat_insulated.gif")
        print("    - heat_conducting.gif")
        print("  Wave equation:")
        print("    - wave_dirichlet_fixed.gif")
        print("    - wave_neumann_reflecting.gif")
        print("    - wave_periodic.gif")
        print("    - wave_absorbing.gif")
        print("    - wave_reflecting.gif")
        print("\nThese animations demonstrate:")
        print("  ✅ Heat conservation with insulated boundaries")
        print("  ✅ Heat loss with conducting boundaries")
        print("  ✅ Wave reflections with reflecting boundaries")
        print("  ✅ Wave absorption with absorbing boundaries")
        print("  ✅ Periodic wrapping effects")
        print("  ✅ Different boundary condition behaviors")
        
    except Exception as e:
        print(f"❌ Demo failed with error: {e}")
        raise


if __name__ == "__main__":
    main()