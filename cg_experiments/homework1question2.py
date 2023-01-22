import numpy as np
from fractions import Fraction
import functools
import os
import psutil
import multiprocessing as mp
from math import radians
from decimal import Decimal
import sympy as sp

from rotation_matrices import *
from scale_matrices import *
from translation_matrices import *
from matrix import *
from equations import *
import cProfile


def main():
    scale = get_non_uniform_scale_matrix(5, 10, 5)

    rotation_x = get_rotation_matrix_x(45)
    rotation_z = get_rotation_matrix_z(30)

    translation = get_translation_matrix(0, 2, 3)

    rotation = rotation_x @ rotation_z

    print("scale\n", scale)
    print("rotation\n", rotation)
    print("translation\n", translation)
    print()

    m = translation @ rotation @ scale
    m_inv = (
        inverse_matrix(scale) @ inverse_matrix(rotation) @ inverse_matrix(translation)
    )

    print("M\n", m)
    print("M inv\n", m_inv)

    o = np.array(
        [
            [5],
            [5],
            [5],
            [1],
        ]
    )

    d = np.array(
        [
            [-4],
            [-2],
            [-4],
            [0],
        ]
    )

    o_l = m_inv @ o
    d_l = m_inv @ d

    print("o_l\n", o_l)
    print("d_l\n", d_l)

    A = np.array([[-0.5], [0], [0.5], [0]])

    t = calc_ray_intersection_with_surface(A, o_l, d_l)
    print("t\n", t)

    print("intersection point\n", sp.N(calc_point_of_intersection(o_l, d_l, t)))


if __name__ == "__main__":
    main()
