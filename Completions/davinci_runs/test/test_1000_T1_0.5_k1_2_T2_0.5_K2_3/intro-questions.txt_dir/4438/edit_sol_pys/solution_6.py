

def read_ints():
    return list(map(int, input().strip().split()))

def read_int():
    return int(input().strip())

def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        matrix.append(read_ints())
    return matrix

def read_tuple(convert=None, types=int):
    if convert is None:
        return tuple(types(i) for i in read_ints())
    return tuple(map(convert, read_ints())

def read_lines(n, consume_last_newline=True):
    lines = []
    for _ in range(n):
        lines.append(input().strip())
        if consume_last_newline:
            input()
    if not consume_last_newline:
        input()
    return lines
def read_string():
    return input().strip()



def main():
    n = read_int()
    points = []
    for _ in range(n):
        points.append(read_tuple(types=float))
    points.sort()
    print(points)
    return


if __name__ == "__main__":
    main()
