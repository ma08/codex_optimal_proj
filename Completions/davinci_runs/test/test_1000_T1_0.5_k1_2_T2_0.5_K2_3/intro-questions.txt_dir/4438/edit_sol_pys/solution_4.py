

def read_ints():
    return list(map(int, input().strip().split(' ')))

def read_int():
    return int(input().strip())

def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(read_ints())
    return matrix

def read_tuple():
    return tuple(read_ints())

def read_lines(n):
    lines = []
    for _ in range(n):
        lines.append(input().strip())
    return lines

def read_string():
    return input().strip()
def read_string_single_line():
    return input().strip()

def read_strings():
    return input().strip().split(' ')


def main():
    n = read_int()
    points = []
    for _ in range(n):
        points.append(read_tuple())
    points.sort()
    print(points)
    return


if __name__ == "__main__":
    main()
