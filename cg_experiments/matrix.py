import sympy as sp
import numpy as np


def inverse_matrix(m: np.ndarray):
    return np.array(sp.Matrix.inv(sp.Matrix(m)))
