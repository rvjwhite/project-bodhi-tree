# examples/creative_demo.py (Corrected and Final)
"""
Bodhi SDK Demo: Goal-Oriented Creative Synthesis

This script demonstrates the core capability of the GCLM v3.0:
solving a creative design problem autonomously.

The GCLM will be tasked with designing a more hydrodynamic boat hull
by creatively blending foundational physics concepts.
"""

import numpy as np
import sys
import os

# Add the root directory to the Python path to allow imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bodhi_sdk.gclm import GCLMv3
from bodhi_sdk.goal import Goal
from bodhi_sdk.spu.dashboard import display_spu_state # The demo now imports the dashboard

# --- 1. Define the Creative Problem ---

def hydrodynamic_fitness(kernel: np.ndarray) -> float:
    test_force = np.array([1.0, 1.0])
    performance_vector = test_force @ kernel.T
    speed, instability = performance_vector[0], abs(performance_vector[1])
    return speed - (instability * 1.5)

boat_design_goal = Goal(
    description="Design a more hydrodynamic boat hull",
    base_kernel_name="M_hull_prototype_v1",
    exploration_kernels=["M_fluid_dynamics_v1", "M_material_rigidity_v1"],
    fitness_function=hydrodynamic_fitness,
    iterations=10
)

# --- 2. Initialize the GCLM and its Knowledge Base ---

gclm_node = GCLMv3(spinor_dim=2)

gclm_node.load_expert_from_dict("M_hull_prototype_v1", {
    "kernel": np.array([[1.2, 0.5], [0.1, 1.1]], dtype=np.float32)
})
gclm_node.load_expert_from_dict("M_fluid_dynamics_v1", {
    "kernel": np.array([[1.5, -0.2], [0.0, 0.9]], dtype=np.float32)
})
gclm_node.load_expert_from_dict("M_material_rigidity_v1", {
    "kernel": np.array([[0.9, 0.0], [0.0, 1.8]], dtype=np.float32)
})

# --- 3. Issue the Creative Challenge with Interpretability ---

print("="*60)
print("      PROJECT BODHI TREE - CREATIVE SYNTHESIS DEMO")
print("="*60)
print(f"TASK: '{boat_design_goal.description}'")
print("\nGCLM will now attempt to invent a superior solution...")

# --- NEW: We will now manually use the dashboard for interpretability ---
base_kernel = gclm_node.local_experts[boat_design_goal.base_kernel_name]['kernel']
explorer_kernel = gclm_node.local_experts[boat_design_goal.exploration_kernels[0]]['kernel']
vspu = gclm_node.spu_driver.vspu

# Show a single composition step visually
print("\n--- Mechanistic Interpretability: Visualizing one composition step ---")
vspu.load_tma(base_kernel)
display_spu_state(vspu, "BEFORE Composition", "Compose fluid_dynamics on hull")
final_matrix = gclm_node.spu_driver.execute_composition(base_kernel, explorer_kernel)
display_spu_state(vspu, "AFTER Composition", "Compose fluid_dynamics on hull")
print("This new matrix is one of many 'ideas' the GCLM will now test.")
# --------------------------------------------------------------------------

# Run the full creative process
solution_packet = gclm_node.solve_creative_problem(boat_design_goal)

# --- 4. Analyze the Result ---

if solution_packet:
    print("\n--- CREATIVE PROCESS COMPLETE ---")
    print("The GCLM has designed a new SPU Kernel to solve the problem.")
    print(f"\nSolution Name: {solution_packet['name']}")
    print(f"Description: {solution_packet['description']}")
    print("\nFinal Optimized Kernel Matrix:")
    print(solution_packet['kernel'])
    print("\nThis new kernel can now be used for hyper-efficient execution on the SPU.")
else:
    print("\n--- CREATIVE PROCESS COMPLETE ---")
    print("The GCLM explored many options but did not find a solution superior to the base prototype.")