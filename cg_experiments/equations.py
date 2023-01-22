from sympy import Matrix, simplify


def calc_ray_intersection_with_surface(p0, o, d, n=Matrix([[0], [1], [0], [0]])):
    numerator = Matrix(Matrix(p0) - Matrix(o)).dot(n)
    denominator = Matrix(d).dot(n)
    return simplify(f"{numerator}/{denominator}")


def calc_point_of_intersection(o, d, t):
    p = Matrix(o) + Matrix(d) * t
    return p[:3]
