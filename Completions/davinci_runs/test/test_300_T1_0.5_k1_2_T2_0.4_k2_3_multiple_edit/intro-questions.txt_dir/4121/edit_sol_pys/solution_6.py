
def solver(n, a, k):
    """
    >>> solver(5, [2, 1, 1, 2, 5], 3)
    'YES'
    >>> solver(3, [4, 5, 3], 2)
    'YES'
    >>> solver(2, [10, 10], 1)
    'YES'
    >>> solver(3, [1, 2, 3], 2)
    'NO'
    """
    if len(set(a)) == 1 or len(set(a)) == k:
        return 'YES'
    if len(set(a)) == k + 1:
        return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(solver(n, a, k))
