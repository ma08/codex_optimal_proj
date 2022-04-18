

def read_ints():
    return list(map(int, input().strip().split()))

def read_int():
    return int(input().strip())

def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(read_ints())
    return matrix

def read_tuple():
    return tuple(read_ints())

def read_lines(n, consume_last_newline=True):
    lines = []
    for _ in range(n):
        lines.append(input().strip())
        if consume_last_newline:
            input()
    if not consume_last_newline:
        input()
    return lines


def main():
    n = read_int()
    points = set()
    for _ in range(n):
        points.add(read_tuple())
    print(points)


if __name__ == "__main__":
    main()
