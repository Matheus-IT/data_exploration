import numpy as np
import sympy as sp
from matrix import inverse_matrix
from scale_matrices import get_non_uniform_scale_matrix
from translation_matrices import get_translation_matrix
from rotation_matrices import get_rotation_matrix_x
from equations import calc_ray_intersection_with_surface, calc_point_of_intersection


def main():
    scale = get_non_uniform_scale_matrix(5, 10, 5)
    print("scale\n", scale)

    rotation = get_rotation_matrix_x(30)

    translation = get_translation_matrix(3, 2, 3)
    print("translation\n", translation)

    m = translation @ rotation @ scale
    print("m\n", m)

    scale_inv = inverse_matrix(scale)
    print("scale_inv\n", scale_inv)

    rotation_inv = inverse_matrix(rotation)
    print("rotation_inv\n", rotation_inv)

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

    points = [
        {"p": np.array([[0], [0], [0.5], [0]]), "n": sp.Matrix([[0], [0], [1], [0]])},
        {"p": np.array([[0], [0], [-0.5], [0]]), "n": sp.Matrix([[0], [0], [-1], [0]])},
        {"p": np.array([[0], [0.5], [0], [0]]), "n": sp.Matrix([[0], [1], [0], [0]])},
        {"p": np.array([[0], [-0.5], [0], [0]]), "n": sp.Matrix([[0], [-1], [0], [0]])},
        {"p": np.array([[0.5], [0], [0], [0]]), "n": sp.Matrix([[1], [0], [0], [0]])},
        {"p": np.array([[-0.5], [0], [0], [0]]), "n": sp.Matrix([[-1], [0], [0], [0]])},
    ]

    for point in points:
        t = calc_ray_intersection_with_surface(point["p"], o_l, d_l, point["n"])
        print("t\n", sp.N(t))
        intersection = calc_point_of_intersection(o_l, d_l, t)
        # print("intersection\n", intersection)
        print("intersection\n", sp.N(sp.Matrix(intersection)))


if __name__ == "__main__":
    main()
