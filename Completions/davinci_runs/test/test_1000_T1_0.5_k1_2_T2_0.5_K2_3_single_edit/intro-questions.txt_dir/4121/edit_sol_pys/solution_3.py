


def solver(n, a):
    """
    >>> solver(5, [1, 1, 2, 2, 5])
    'YES'
    >>> solver(3, [4, 5, 3])
    'YES'
    >>> solver(2, [10, 10])
    'YES'
    >>> solver(3, [1, 2, 3])
    >>> solver(4, [1, 2, 3, 4])
    'NO'
    >>> solver(4, [1, 2, 3, 4])
    'NO'
    >>> solver(4, [10, 10, 10, 10])
    'YES'
    >>> solver(4, [10, 10, 10, 10])
    'YES'
    >>> solver(4, [10, 10, 10, 10])
    'YES'
    >>> solver(4, [10, 10, 10, 10])
    'YES'
    'NO'
    """
    if len(set(a)) == 1:
        return 'YES'
    elif len(set(a)) == 2:
        if a.count(max(set(a))) == 1 and min(set(a)) == 1:
            return 'YES'    
    elif len(set(a)) > 2:
    return 'NO'
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
