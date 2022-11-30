import sys
from math import sqrt


def read_numbers(input_data: str):
    return list(map(int, input_data.strip().split(' ')))


def compute_distance_between_centers(x1, y1, x2, y2):
    """Calculate the distance between the centers of the elipses"""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def elipses_match(centers_distance, r1, r2):
    """Tells if one elipse is inside the other"""
    return centers_distance <= r1 - r2


for line in sys.stdin:
    input_data = str(line)
    if not input_data:
        break

    r1, x1, y1, r2, x2, y2 = read_numbers(input_data)

    centers_distance = compute_distance_between_centers(x1, y1, x2, y2)

    match = elipses_match(centers_distance, r1, r2)

    results = {
        False: 'MORTO',
        True: 'RICO',
    }

    print(results[match])
