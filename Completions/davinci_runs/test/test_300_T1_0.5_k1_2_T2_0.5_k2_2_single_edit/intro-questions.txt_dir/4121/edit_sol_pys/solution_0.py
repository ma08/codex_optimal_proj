
import doctest


def solver(n, a):
    """
    >>> solver(5, [2, 1, 1, 2, 5])
    'YES'
    >>> solver(3, [4, 5, 3])
    'YES'
    >>> solver(2, [10, 10])
    'YES'
    >>> solver(3, [1, 2, 3])
    'NO'
    if len(set(a)) == 0:
        return 'NO'
    """
    if len(set(a)) == 1:
        return 'YES'
    if len(set(a)) == 2:
        if a.count(max(set(a))) == 1:
            return 'YES'
        else:
            return 'NO'
    if len(set(a)) > 2:
        return 'NO'


if __name__ == "__main__":
    n = int(input())

    doctest.testmod()
    a = list(map(int, input().split()))
    print(solver(n, a))
