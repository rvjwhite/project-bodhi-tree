# bodhi_sdk/gclm.py (Corrected)

from .goal import Goal
from .causal_engine import CausalInferenceEngine
from .spu.driver import SPUDriver
from .assembly_module import AssemblyModule

class GCLMv3:
    """Represents a single instance of the Geometric-Causal Language Model."""
    def __init__(self, spinor_dim=4, enable_dashboard=True): # Pass flag here
        print("\nInitializing Project Bodhi Tree GCLM v3.0 instance...")
        self.cie = CausalInferenceEngine()
        # The GCLM now creates the driver but doesn't use the dashboard itself
        self.spu_driver = SPUDriver(spinor_dim=spinor_dim) 
        self.assembler = AssemblyModule()
        self.local_experts = {}
        print("GCLM Instance Ready.")
        
    # ... (rest of the file is unchanged, as it correctly calls the driver)
    def load_expert_from_dict(self, expert_name, expert_data):
        """Loads a pre-defined expert into the local library."""
        print(f"GCLM: Loading expert '{expert_name}' into local library.")
        self.local_experts[expert_name] = expert_data

    def solve_creative_problem(self, goal: Goal):
        """Top-level method to engage the GCLM in goal-oriented creative synthesis."""
        print(f"\n--- GCLM Creative Challenge Initiated: {goal.description} ---")
        
        # 1. Ensure we have all the necessary foundational kernels
        self.acquire_expertise(goal.base_kernel_name)
        for name in goal.exploration_kernels:
            self.acquire_expertise(name)
            
        # 2. Engage the Causal Inference Engine's Synthesis Planner
        solution_packet = self.cie.directed_synthesis(goal, self.local_experts, self.assembler)
        
        # 3. If a solution is found, report it.
        if solution_packet:
            print(f"\nGCLM: Creative solution '{solution_packet['name']}' discovered.")
            # In a real system, this would be pushed to the GEC
            return solution_packet
        else:
            print("\nGCLM: Creative process did not yield a superior solution.")
            return None

    def acquire_expertise(self, expert_name):
        """Simulates ensuring expertise is available locally."""
        if expert_name not in self.local_experts:
            # This is where the GEC_Client would be called in a real system.
            raise ValueError(f"Expertise '{expert_name}' not found in local library. GEC pull needed.")
        return True