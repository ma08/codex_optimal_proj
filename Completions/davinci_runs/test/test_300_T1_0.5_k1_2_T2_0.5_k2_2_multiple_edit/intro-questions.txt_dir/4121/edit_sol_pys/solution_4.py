


def solver(n, a, x, y):
    """
    >>> solver(3, [1, 2, 3], 1, 2)
    1
    >>> solver(3, [1, 2, 3], 2, 3)
    1
    >>> solver(4, [4, 3, 2, 1], 2, 3)
    2
    >>> solver(4, [4, 3, 2, 1], 1, 3)
    3
    >>> solver(4, [4, 3, 2, 1], 1, 2)
    4
    """

    count = 0
    while a[x-1] != y:
        a[x-1], x = a[x-1], a[x-1]
        count += 1
    return count


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    x, y = map(int, input().split())
    print(solver(n, a, x, y))
