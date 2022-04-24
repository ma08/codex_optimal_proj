
import numpy as np


def main():
    n = int(input())
    a = np.full((n, 2), -1, dtype=int)
    for i in range(n):
        a[i, 0], a[i, 1] = map(int, input().split())
    p = np.full(n, -1, dtype=int)  # path
    p[0] = 1  # first element
    p[1] = a[0, 0]  # second element
    p[2] = a[0, 1]  # third element
    for i in range(2, n):  # next elements
        p[i] = a[p[i - 1] - 1, 0] if a[p[i - 1] - 1, 0] != p[i - 2] else a[p[i - 1] - 1, 1]  # path formula
    print(*p)  # print path


if __name__ == '__main__':
    main()
