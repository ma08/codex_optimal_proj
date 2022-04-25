
def solver(n, a, b):
    """
    >>> solver(3, [3, 2, 1], [2, 3, 1])
    '1 2 3'
    >>> solver(3, [3, 2, 1], [1, 2, 3])
    '1 2 3'
    >>> solver(3, [2, 3, 1], [1, 2, 3])
    '1 2 3'
    >>> solver(3, [1, 2, 3], [3, 2, 1])
    '1 2 3'
    >>> solver(3, [1, 2, 3], [2, 3, 1])
    '1 2 3'
    >>> solver(3, [2, 3, 1], [3, 2, 1])
    '1 2 3'
    """
    ans = []
    for i in range(n):
        ans.append(a[i] + b[i])
    return ' '.join(map(str, ans))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))  # a[i]
    b = list(map(int, input().split()))  # b[i]
    print(solver(n, a, b))
