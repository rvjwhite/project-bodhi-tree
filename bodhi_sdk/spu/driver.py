# bodhi_sdk/spu/driver.py (Corrected)

from .virtual_spu import VirtualSPU
import numpy as np

class SPUDriver:
    """
    Software driver for the Virtual SPU.
    This class is the sole interface between the GCLM software and the SPU hardware.
    """
    def __init__(self, spinor_dim=4):
        print("SPU DRIVER: Initializing Virtual SPU...")
        self.vspu = VirtualSPU(spinor_dim)
        print("SPU DRIVER: Ready.")

    def execute_transform(self, kernel_matrix: np.ndarray, input_vector: np.ndarray) -> np.ndarray:
        """Executes a single matrix-vector product on the V-SPU."""
        self.vspu.load_tma(kernel_matrix)
        self.vspu.load_svr(input_vector)
        result = self.vspu.execute_vector_mode()
        return result

    def execute_composition(self, kernel_m1: np.ndarray, kernel_m2: np.ndarray) -> np.ndarray:
        """Executes a matrix-matrix product on the V-SPU."""
        # M1 is loaded into the TMA first
        self.vspu.load_tma(kernel_m1)
        result = self.vspu.execute_composition_mode(kernel_m2)
        return result