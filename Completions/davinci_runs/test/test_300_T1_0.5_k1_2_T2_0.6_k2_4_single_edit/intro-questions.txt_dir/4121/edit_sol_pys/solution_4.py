

def solver(n, a, k):
    """
    >>> solver(5, [2, 1, 1, 2, 5], 3)
    'YES'
    >>> solver(3, [4, 5, 3], 2)
    'YES'
    >>> solver(2, [10, 10], 2)
    'YES'
    >>> solver(3, [1, 2, 3], 2)
    'NO'
    """
    if len(set(a)) == 1 and k % 2 == 0:
        return 'YES'
        if k % 2 == 0:
            return 'NO'
        return 'YES'
    if len(set(a)) > 2:
        return 'YES'


    k = int(input())
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a, k))
