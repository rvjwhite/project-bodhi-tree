# bodhi_sdk/goal.py

from dataclasses import dataclass
from typing import Callable, Dict
import numpy as np

@dataclass
class Goal:
    """A structured representation of a creative problem to be solved."""
    description: str
    base_kernel_name: str
    exploration_kernels: list
    fitness_function: Callable[[np.ndarray], float]
    iterations: int = 15