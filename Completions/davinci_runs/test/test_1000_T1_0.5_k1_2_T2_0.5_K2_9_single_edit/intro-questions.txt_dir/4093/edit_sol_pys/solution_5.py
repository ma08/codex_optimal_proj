

import sys
import math


def solve(n, m):
    return (n - 1) * (m - 1)


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        print(solve(n, m))
