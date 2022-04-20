
import sys
import math

def solve(n, k, a):
    """
    >>> solve(6, 11, [45, 1, 10, 12, 11, 7])
    7
    >>> solve(4, 2, [2, 78, 4, 10])
    12
    >>> solve(5, 2, [3, 7, 19, 3, 3])
    0
    """
    return 0


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    print(solve(n, k, a))
