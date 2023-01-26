import numpy as np
import sympy as sp
from matrix import inverse_matrix
from scale_matrices import *
from translation_matrices import get_translation_matrix
from rotation_matrices import get_rotation_matrix_x
from equations import *


def main():
    scale = get_non_uniform_scale_matrix(10, 5, -5)
    print("scale\n", scale)

    rotation = get_rotation_matrix_x(90)
    print("rotation\n", rotation)

    translation = get_translation_matrix(0, 1, 3)
    print("translation\n", translation)

    m = translation @ rotation @ scale
    print("m\n", m)

    scale_inv = inverse_matrix(scale)
    print("scale_inv\n", scale_inv)

    rotation_inv = inverse_matrix(rotation)
    print("rotation inv\n", rotation_inv)

    translation_inv = inverse_matrix(translation)
    print("translation_inv\n", translation_inv)

    m_inv = scale_inv @ rotation_inv @ translation_inv
    print("m_inv\n", m_inv)

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
            [sp.simplify(f"-{2}/{3}")],
            [sp.simplify(f"-{1}/{3}")],
            [sp.simplify(f"-{2}/{3}")],
            [0],
        ]
    )

    o_l = m_inv @ o
    d_l = m_inv @ d

    print("o_l\n", o_l)
    print("d_l\n", d_l)

    t = calc_ray_intersection_with_sphere(d_l, o_l)
    # print("t\n", sp.N(sp.Matrix(t)))
    print("t\n", t)
    # intersection = calc_point_of_intersection(o_l, d_l, t)
    # print("intersection\n", intersection)
    # print("intersection\n", sp.N(sp.Matrix(intersection)))


if __name__ == "__main__":
    main()
