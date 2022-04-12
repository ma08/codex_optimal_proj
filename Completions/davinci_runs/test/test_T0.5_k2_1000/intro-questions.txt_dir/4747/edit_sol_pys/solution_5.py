
import sys

def solve(n, k):
    """
    >>> solve(1, 1)
    1
    >>> solve(2, 1)
    1.0
    >>> solve(2, 2)
    1.5
    >>> solve(3, 2)
    2.0
    """
    res = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            res += i * (1.0 / n) * (1.0 / n) * (1.0 / n) * (1.0 / n) * (1.0 / n)
    return res

if __name__ == '__main__':
    if len(sys.argv) > 1:
        import doctest
        doctest.testmod()
    else:
        n, k = map(int, sys.stdin.readline().split())
        print solve(n, k)
