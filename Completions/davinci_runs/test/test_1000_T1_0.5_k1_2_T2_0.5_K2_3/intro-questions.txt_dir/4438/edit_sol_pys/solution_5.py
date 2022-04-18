

def read_ints():
    return list(map(int, input().strip().split()))

def read_int():
    return int(input().strip())

def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(read_ints())
    return matrix

def read_tuple(convert=None):
    if convert is None:
        return tuple(read_ints())
    return tuple(map(convert, read_ints()))

def read_lines(n, consume_last_newline=True):
    lines = []
    for _ in range(n):
        lines.append(input().strip())
        if consume_last_newline and _ < n - 1:
            input()
    if not consume_last_newline and n > 0:
        input()
    return lines


def main():
    n = read_int()
    points = []
    for _ in range(n):
        points.append(read_tuple())
    points.sort()
    print(points[0][0])
    return


if __name__ == "__main__":
    main()
