import sys


sys.stdin = open('input.txt')
sys.stdout = open('output.txt', 'w')


def read_int():
    return int(input().strip())


def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return matrix


def read_lines(n):
    lines = []
    for _ in range(n):
        lines.append(input().strip())
    return lines


def main():
    n = read_int()
    print(n)
    return


if __name__ == "__main__":
    main()
