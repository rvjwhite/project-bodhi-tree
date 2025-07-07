# bodhi_sdk/spu/driver.py

from .virtual_spu import VirtualSPU
from .dashboard import display_spu_state
import numpy as np

class SPUDriver:
    """Software driver for the Virtual SPU."""
    def __init__(self, spinor_dim=4, enable_dashboard=True):
        print("SPU DRIVER: Initializing Virtual SPU...")
        self.vspu = VirtualSPU(spinor_dim)
        self.enable_dashboard = enable_dashboard
        print("SPU DRIVER: Ready.")

    def execute_transform(self, kernel_matrix: np.ndarray, input_vector: np.ndarray) -> np.ndarray:
        """Executes a single matrix-vector product on the V-SPU."""
        op_str = f"Transform Vector w/ Kernel"
        if self.enable_dashboard:
            display_spu_state(self.vspu, "State BEFORE Transform", op_str)
        
        self.vspu.load_tma(kernel_matrix)
        self.vspu.load_svr(input_vector)
        result = self.vspu.execute_vector_mode()
        
        if self.enable_dashboard:
            display_spu_state(self.vspu, "State AFTER Transform", op_str)
            
        return result

    def execute_composition(self, kernel_m1: np.ndarray, kernel_m2: np.ndarray) -> np.ndarray:
        """Executes a matrix-matrix product on the V-SPU."""
        op_str = f"Compose M2 onto M1"
        if self.enable_dashboard:
            display_spu_state(self.vspu, "State BEFORE Composition", op_str)
            
        self.vspu.load_tma(kernel_m1)
        result = self.vspu.execute_composition_mode(kernel_m2)
        
        if self.enable_dashboard:
            display_spu_state(self.vspu, "State AFTER Composition", op_str)
            
        return result