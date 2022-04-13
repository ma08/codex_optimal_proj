
import sys, math

def solve(n, k):
    """
    >>> solve(1, 1)
    1
    >>> solve(2, 3)
    1.875
    >>> solve(6, 2)
    4.25
    """
    res = 0
    for i in xrange(1, k+1):
        res += i * math.pow(1.0 / n, 6)
    return res * n

if __name__ == '__main__':
    if len(sys.argv) > 1:
        import doctest
        doctest.testmod()
    else:
        n, k = map(int, sys.stdin.readline().split())
        print solve(n, k)
