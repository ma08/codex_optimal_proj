

import sys

def solve(H, n, d):
    """
    >>> solve(1000, 6, [-100, -200, -300, 125, 77, -4])
    9
    >>> solve(1000000000000, 5, [-1, 0, 0, 0, 0])
    4999999999996
    >>> solve(10, 4, [-3, -6, 5, 4])
    -1
    """
    k = 0
    while H > 0:
        if k == n:
            k = 0
        H += d[k]
        k += 1
    if H <= 0:
        return k
    else:
        return -1

if __name__ == "__main__":
    H, n = map(int, sys.stdin.readline().strip().split(' '))
    d = map(int, sys.stdin.readline().strip().split(' '))
    print solve(H, n, d)