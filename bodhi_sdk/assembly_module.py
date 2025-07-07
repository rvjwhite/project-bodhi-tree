# bodhi_sdk/assembly_module.py

import numpy as np

class AssemblyModule:
    """Implements the Assembly of Experts (AoE) model merging logic for SPU Kernels."""
    def __init__(self):
        # This module is currently stateless.
        pass

    def merge_kernels(self, kernel_a: np.ndarray, kernel_b: np.ndarray, ratio_b: float) -> np.ndarray:
        """
        Merges two SPU kernel matrices using linear interpolation.
        """
        if not (0.0 <= ratio_b <= 1.0):
            raise ValueError("ratio_b must be between 0.0 and 1.0.")
        if kernel_a.shape != kernel_b.shape:
             raise ValueError("Kernels must have the same shape to be merged.")
            
        composite_kernel = (1 - ratio_b) * kernel_a + ratio_b * kernel_b
        return composite_kernel