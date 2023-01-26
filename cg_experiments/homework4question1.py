import numpy as np
import sympy as sp
from matrix import inverse_matrix
from scale_matrices import *
from translation_matrices import get_translation_matrix
from rotation_matrices import *
from equations import *


def main():
    scale = get_non_uniform_scale_matrix(1, 5, 1)
    print("scale\n", scale)

    translation = get_translation_matrix(0, 4, 0)
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

    t = calc_ray_intersection_with_cylinder(d_l, o_l)
    print("cylinder t\n", t)

    t_l = get_the_smallest(t)

    print("smallest", t_l)

    interception_point = calc_point_of_intersection(o_l, d_l, t_l)

    print("interception_point", sp.N(sp.Matrix(interception_point)))

    # now we're going to try to calculate the intersection with the top surface

    A = np.array([[0], [0.5], [0], [0]])

    t = calc_ray_intersection_with_surface(A, o_l, d_l)
    print("surface t\n", t)

    interception_point = calc_point_of_intersection(o_l, d_l, t)

    print("interception_point", interception_point)

    print(calc_interception_with_circle(interception_point))

    # since there's no interception now i'm going to calculate the interception
    # with the bottom surface
    A = np.array([[0], [-0.5], [0], [0]])

    t = calc_ray_intersection_with_surface(A, o_l, d_l, n=sp.Matrix([0, -1, 0, 0]))
    print("surface t\n", t)

    interception_point = calc_point_of_intersection(o_l, d_l, t)
    print("interception_point", interception_point)

    print(calc_interception_with_circle(interception_point))


if __name__ == "__main__":
    main()
