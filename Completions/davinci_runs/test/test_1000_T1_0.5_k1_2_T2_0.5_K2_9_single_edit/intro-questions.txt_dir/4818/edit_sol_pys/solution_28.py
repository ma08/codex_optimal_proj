
import sys


def main():
    n = int(input())
    m = int(input())
    matrix = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    print(matrix)


if __name__ == '__main__':
    main()
