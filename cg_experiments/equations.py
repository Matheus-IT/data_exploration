from sympy import Matrix


def calc_ray_equation(p0, o, d, n=Matrix([[0], [1], [0], [0]])):
    numerator = Matrix(Matrix(p0) - Matrix(o)).dot(n)
    denominator = Matrix(d).dot(n)
    return numerator / denominator
