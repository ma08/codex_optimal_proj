
import sys
sys.setrecursionlimit(10**6)



def solver(n, a, x, y, count=0):
    """
    >>> solver(3, [1, 2, 3], 1, 2, count=0)
    1
    >>> solver(3, [1, 2, 3], 2, 3, count=0)
    1
    >>> solver(4, [4, 3, 2, 1], 2, 3, count=0)
    2
    >>> solver(4, [4, 3, 2, 1], 1, 3, count=0)
    3
    >>> solver(4, [4, 3, 2, 1], 1, 2, count=0)
    4
    """

    while a[x-1] != y:
        a[x-1], x = a[x-1], a[x-1]
        count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    a, x, y = map(int, input().split())
    print(solver(n, a, x, y))
