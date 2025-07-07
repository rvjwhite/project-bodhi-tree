# bodhi_sdk/spu/virtual_spu.py

import numpy as np
import time

class VirtualSPU:
    """A high-level simulation of the Spinor Processing Unit v2.0."""
    def __init__(self, spinor_dim=4):
        self.spinor_dim = spinor_dim
        self.TMA = np.zeros((spinor_dim, spinor_dim))
        self.SVR = np.zeros(spinor_dim)
        self.OutputRegister = np.zeros((spinor_dim, spinor_dim))
        self.LATENCY_CIM_NS = 5
        self.LATENCY_LOAD_NS = 2

    def _simulate_latency(self, ns):
        # Using a very small sleep to simulate time without halting the demo too much
        time.sleep(ns / 1e9) 

    def load_tma(self, matrix: np.ndarray):
        if matrix.shape != (self.spinor_dim, self.spinor_dim):
            raise ValueError("Matrix dimensions do not match SPU configuration.")
        self.TMA = matrix
        self._simulate_latency(self.LATENCY_LOAD_NS)

    def load_svr(self, vector: np.ndarray):
        self.SVR = vector
        self._simulate_latency(self.LATENCY_LOAD_NS)

    def execute_vector_mode(self):
        self.OutputRegister = self.SVR @ self.TMA.T
        self._simulate_latency(self.LATENCY_CIM_NS)
        return self.OutputRegister.copy()

    def execute_composition_mode(self, matrix_m2: np.ndarray):
        m1 = self.TMA
        composite_matrix = np.zeros_like(m1)
        
        for j in range(self.spinor_dim):
            col_m2 = matrix_m2[:, j]
            self.load_svr(col_m2)
            result_col = self.SVR @ m1.T
            self._simulate_latency(self.LATENCY_CIM_NS)
            composite_matrix[:, j] = result_col
            
        self.OutputRegister = composite_matrix
        return self.OutputRegister.copy()