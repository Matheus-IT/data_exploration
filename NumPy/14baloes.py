# Utils ---------------------------------------------------------------
def read_numbers():
    try:
        input_data = input()
    except EOFError:
        return []
    return list(map(int, input_data.split(' ')))


# ---------------------------------------------------------------------

while True:
    input_data = read_numbers()
    if not input_data:
        break
    line_segments, queries = input_data
    print(line_segments, queries)

    for i in range(line_segments):
        x1, y1, x2, y2 = read_numbers()
        print(x1, y1, x2, y2)

    for i in range(queries):
        query = read_numbers()[0]
        print(query)
