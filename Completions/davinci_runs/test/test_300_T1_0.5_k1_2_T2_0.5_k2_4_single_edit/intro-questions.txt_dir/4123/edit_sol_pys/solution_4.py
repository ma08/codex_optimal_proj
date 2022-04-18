
def solve(s):
    """
    >>> solve(3, [1, 2, 3])
    0
    >>> solve(3, [1, 1, 1])
    1
    >>> solve(3, [1, 2, 1])
    2
    """
    return 0


if __name__ == "__main__":
    n, *a = map(int, open(0).read().split())
    result = solve(n, a)
    print(result)
