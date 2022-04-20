def solver(n, a):
    """
    >>> solver(5, [1, 1, 2, 2, 3])
    3
    >>> solver(3, [3, 3, 3])
    1
    >>> solver(4, [4, 4, 4, 4])
    1
    """
    kinds = len(set(a))
    if kinds == 1:
        return 1
    if kinds == 2:
        return 2
    if kinds == 3:
        return 3


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
