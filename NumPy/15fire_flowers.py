import sys


def read_numbers(input_data: str):
    return list(map(int, input_data.strip().split(' ')))


for line in sys.stdin:
    input_data = str(line)
    if not input_data:
        break

    r1, x1, y1, r2, x2, y2 = read_numbers(input_data)
    print(r1, x1, y1, r2, x2, y2)
