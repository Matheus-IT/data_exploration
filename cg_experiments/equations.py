import sympy as sp
from sympy import lambdify, Matrix


def sympy_to_numpy():
    from sympy.abc import x, y

    g = sp.Matrix()
    s = (x, y)
    g_func = lambdify(s, g, modules="numpy")


def calc_ray_equation(p0, o, d, n=Matrix([[0], [1], [0], [0]])):
    numerator = Matrix(Matrix(p0) - Matrix(o)).dot(n)
    denominator = Matrix(d).dot(n)
    return numerator / denominator
