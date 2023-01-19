from sympy import lambdify, Matrix


def sympy_to_numpy():
    from sympy.abc import x, y

    g = Matrix()
    s = (x, y)
    g_func = lambdify(s, g, modules="numpy")
