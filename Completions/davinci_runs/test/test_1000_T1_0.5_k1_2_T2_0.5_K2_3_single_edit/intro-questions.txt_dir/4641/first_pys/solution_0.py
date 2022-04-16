

import sys

def solve(queries, x):
    """
    >>> solve([0, 1, 2, 2, 0, 0, 10], 3)
    [1, 2, 3, 3, 4, 4, 7]
    >>> solve([1, 2, 1, 2], 3)
    [0, 0, 0, 0]
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