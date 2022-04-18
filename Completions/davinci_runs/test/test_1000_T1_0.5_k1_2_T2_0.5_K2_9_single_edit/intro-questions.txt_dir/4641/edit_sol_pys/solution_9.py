

import sys

def solve(queries, x):
    """
    >>> solve([1, 2], 3)
    [1, 2]
    >>> solve([1, 1], 3)
    [1, 1]
    >>> solve([1, 1, 1], 3)
    [1, 1, 1]
    """
    res = []
    current_mex = 0
    for query in queries:
        if query == current_mex:
            current_mex += 1
        res.append(current_mex)
    return res

if __name__ == '__main__':
    q, x = map(int, sys.stdin.readline().split())
    queries = []
    for _ in range(q):
        queries.append(int(sys.stdin.readline()))
    print('\n'.join(map(str, solve(queries, x))))
