from collections import Counter


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
    counter = Counter(a)
    if len(counter) == 1 or len(counter) == 2:
        if counter.most_common()[0][1] == 1 or counter.most_common()[0][1] == n - 1:
            return 'YES'
    return 'NO'


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solver(n, a))
