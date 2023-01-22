import numpy as np
import sympy as sp
from matrix import inverse_matrix
from scale_matrices import get_uniform_scale_matrix
from translation_matrices import get_translation_matrix
from equations import calc_ray_intersection_with_surface, calc_point_of_intersection


def main():
    scale = get_uniform_scale_matrix(2)
    print("scale\n", scale)

    translation = get_translation_matrix(2, 2, 0)
    print("translation\n", translation)

    m = translation @ scale
    print("m\n", m)

    scale_inv = inverse_matrix(scale)
    print("scale_inv\n", scale_inv)

    translation_inv = inverse_matrix(translation)
    print("translation_inv\n", translation_inv)

    m_inv = scale_inv @ translation_inv
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
        print("t\n", t)
        intersection = calc_point_of_intersection(o_l, d_l, t)
        print("intersection\n", sp.N(sp.Matrix(intersection)))


if __name__ == "__main__":
    main()
