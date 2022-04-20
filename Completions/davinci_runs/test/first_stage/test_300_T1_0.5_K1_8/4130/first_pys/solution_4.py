

def solve(n, a):
    """
    >>> solve(4, [3, 2, 4, 1])
    4
    >>> solve(6, [1, 1, 1, 4, 4, 4])
    5
    >>> solve(5, [1, 2, 3, 4, 5])
    5
    >>> solve(5, [5, 4, 3, 2, 1])
    5
    >>> solve(5, [1, 1, 2, 2, 2])
    4
    >>> solve(5, [1, 2, 3, 4, 3])
    4
    """
    a_set = set(a)
    a_set_size = len(a_set)
    if a_set_size == n:
        return n
    min_a = min(a_set)
    max_a = max(a_set)
    if max_a - min_a + 1 == a_set_size:
        return a_set_size
    else:
        return a_set_size + 1

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))