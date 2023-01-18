import numpy as np
from my_trigonometry import cos, sin


def get_rotation_matrix_z(angle):
    return np.array(
        [
            [cos(angle), -sin(angle), 0],
            [sin(angle), cos(angle), 0],
            [0, 0, 1],
        ]
    )


def get_rotation_matrix_x(angle):
    return np.array(
        [
            [1, 0, 0],
            [0, cos(angle), -sin(angle)],
            [0, sin(angle), cos(angle)],
        ]
    )


def get_rotation_matrix_y(angle):
    return np.array(
        [
            [cos(angle), 0, sin(angle)],
            [0, 1, 0],
            [-sin(angle), 0, cos(angle)],
        ]
    )
