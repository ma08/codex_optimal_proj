
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
    """
    a_set = set(a)
    if len(a_set) == 1:
        return 'YES'
    if len(a_set) == 2:
        if a.count(max(a_set)) == 1:
            return 'YES'
        else:
            return 'NO'
    if len(a_set) > 2:
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
