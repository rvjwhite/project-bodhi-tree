# bodhi_sdk/causal_engine.py

import numpy as np
from .goal import Goal
from .assembly_module import AssemblyModule

class CausalInferenceEngine:
    """Analyzes outcomes and directs the creative synthesis process."""
    def __init__(self, novelty_threshold=0.1):
        self.novelty_threshold = novelty_threshold

    def directed_synthesis(self, goal: Goal, local_kernel_library: dict, assembler: AssemblyModule):
        """The Synthesis Planner. Uses a creative loop to find an optimal solution."""
        print(f"\nCIE (Synthesis Planner): Received new goal: '{goal.description}'")
        print(f"CIE: Starting with base kernel '{goal.base_kernel_name}' for {goal.iterations} iterations.")
        
        base_kernel = local_kernel_library[goal.base_kernel_name]['kernel']
        best_solution_kernel = base_kernel
        best_score = goal.fitness_function(base_kernel)
        
        print(f"CIE: Initial score for base kernel: {best_score:.4f}")

        for i in range(goal.iterations):
            explorer_name = np.random.choice(goal.exploration_kernels)
            explorer_kernel = local_kernel_library[explorer_name]['kernel']
            ratio = np.random.rand()
            
            candidate_kernel = assembler.merge_kernels(base_kernel, explorer_kernel, ratio)
            score = goal.fitness_function(candidate_kernel)
            
            print(f"CIE: Iter {i+1:02d} | Blend w/ '{explorer_name}' (ratio {ratio:.2f}) | Score: {score:.4f}")
            
            if score > best_score:
                best_score = score
                best_solution_kernel = candidate_kernel
                print(f"CIE: <<< New best solution found! Score: {best_score:.4f} >>>")

        print("\nCIE: Directed synthesis complete.")
        
        # Check if the final solution is actually better than the starting point
        if best_score > goal.fitness_function(base_kernel):
            discovery_name = f"Optimized_{goal.base_kernel_name}_v1"
            discovery_packet = {
                "name": discovery_name,
                "type": "SPU_KERNEL", "domain": "optimized_design",
                "description": f"An optimized kernel for '{goal.description}' with score {best_score:.4f}",
                "kernel": best_solution_kernel
            }
            return discovery_packet
        return None