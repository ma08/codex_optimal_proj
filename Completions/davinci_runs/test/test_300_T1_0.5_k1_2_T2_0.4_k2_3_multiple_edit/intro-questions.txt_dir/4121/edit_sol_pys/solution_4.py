


def solver(n, a, b):
    """
    >>> solver(5, [2, 1, 1, 2, 5], [1, 2, 3, 4, 5])
    'YES'
    >>> solver(3, [4, 5, 3], [1, 2, 3])
    'YES'
    >>> solver(2, [10, 10], [1, 2])
    'YES'
    >>> solver(3, [1, 2, 3], [1, 2, 3])
    'NO'
    """
    if len(set(a)) == 1 or len(set(b)) == 1:
        return 'YES'
    if a.count(max(set(a))) == 1 or b.count(max(set(b))) == 1:
        return 'YES'
    else:
        return 'NO'
    if len(set(a)) > 2 or len(set(b)) > 2:
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solver(n, a, b))
