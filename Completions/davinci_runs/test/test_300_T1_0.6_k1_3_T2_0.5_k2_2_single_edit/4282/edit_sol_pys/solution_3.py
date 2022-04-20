

import numpy as np


def main():
    n = int(input())
    a = np.zeros((n, 2), dtype=np.int)
    for i in range(n):
        a[i, 0], a[i, 1] = map(int, input().split())
    p = np.full(n, -1, dtype=np.int)
    p[0] = 1
    p[1] = a[0, 0]
    p[2] = a[0, 1]
    for i in range(2, n):
        p[i] = a[p[i - 1] - 1, 0] if a[p[i - 1] - 1, 0] != p[i - 2] else a[p[i - 1] - 1, 1]
    print(*p)


if __name__ == '__main__':
    main()
