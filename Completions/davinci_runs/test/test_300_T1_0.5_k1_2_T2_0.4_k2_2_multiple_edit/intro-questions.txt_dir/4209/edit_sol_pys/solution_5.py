

import sys

def solve(n, a):
    """
    >>> solve(7, [4, 1, 2, 2, 1, 5, 3]) #doctest: +NORMALIZE_WHITESPACE
    3
    7 7
    2 3
    4 5
    >>> solve(11, [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) #doctest: +NORMALIZE_WHITESPACE
    2
    3 4
    1 1
    >>> solve(4, [1, 1, 1, 1]) #doctest: +NORMALIZE_WHITESPACE
    4
    4 4
    1 1
    2 2
    3 3
    """
    pass

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, a)
