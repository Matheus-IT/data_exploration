import numpy as np


def get_non_uniform_scale_matrix(x, y, z):
    return np.array(
        [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1],
        ]
    )


def get_uniform_scale_matrix(amount):
    return np.array(
        [
            [amount, 0, 0, 0],
            [0, amount, 0, 0],
            [0, 0, amount, 0],
            [0, 0, 0, 1],
        ]
    )
