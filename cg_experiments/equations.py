from sympy import Matrix, simplify, solve, Symbol


def calc_ray_intersection_with_surface(p0, o, d, n=Matrix([[0], [1], [0], [0]])):
    numerator = Matrix(Matrix(p0) - Matrix(o)).dot(n)
    denominator = Matrix(d).dot(n)
    return simplify(f"{numerator}/{denominator}")


def calc_point_of_intersection(o, d, t):
    p = Matrix(o) + Matrix(d) * t
    return p[:3]


def calc_ray_intersection_with_sphere(d, o):
    d, o = Matrix(d), Matrix(o)

    a = d.dot(d)
    b = 2 * o.dot(d)
    c = o.dot(o) - 1

    x = Symbol("x")

    return solve(a * x**2 + b * x + c)


def calc_ray_intersection_with_cylinder(d, o):
    from sympy.abc import x

    d, o = Matrix(d), Matrix(o)

    dx, dz = d[0], d[2]
    ox, oz = o[0], o[2]

    a = dx**2 + dz**2
    b = 2 * ox * dx + 2 * oz * dz
    c = ox**2 + oz**2 - 1

    return solve(a * x**2 + b * x + c, x)
