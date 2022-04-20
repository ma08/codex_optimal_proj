

def min_days(n, m, a):
    """Return the minimum number of days Polycarp needs to write his coursework.

    >>> min_days(5, 8, [2, 3, 1, 1, 2])
    4
    >>> min_days(7, 10, [1, 3, 4, 2, 1, 4, 2])
    2
    >>> min_days(5, 15, [5, 5, 5, 5, 5])
    1
    >>> min_days(5, 16, [5, 5, 5, 5, 5])
    2
    >>> min_days(5, 26, [5, 5, 5, 5, 5])
    -1
    """
    # TODO: implement this
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_days(n, m, a))