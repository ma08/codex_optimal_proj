

import sys

def possible(C, n, stations):
    """
    >>> possible(1, 2, [[0, 1, 1], [1, 0, 0]])
    'possible'
    >>> possible(1, 2, [[1, 0, 0], [0, 1, 0]])
    'impossible'
    >>> possible(1, 2, [[0, 1, 0], [1, 0, 1]])
    'impossible'
    >>> possible(2, 4, [[0, 1, 0], [0, 1, 0], [1, 0, 0], [0, 0, 0]])
    'impossible'
    >>> possible(1, 3, [[0, 1, 0], [0, 1, 0], [1, 0, 0]])
    'possible'
    >>> possible(1, 3, [[0, 1, 0], [0, 1, 1], [1, 0, 0]])
    'impossible'
    >>> possible(1, 3, [[0, 1, 0], [1, 0, 1], [1, 0, 0]])
    'impossible'
    >>> possible(1, 3, [[0, 1, 0], [0, 1, 0], [1, 0, 1]])
    'impossible'
    >>> possible(1, 3, [[0, 1, 0], [0, 1, 0], [0, 0, 1]])
    'impossible'
    >>> possible(1, 3, [[0, 1, 0], [0, 1, 0], [0, 1, 1]])
    'impossible'
    """
    for i in range(n):
        if stations[i][2] > 0 and stations[i][1] > 0:
            return "impossible"
        if stations[i][0] > C:
            return "impossible"
        if stations[i][2] > 0 and stations[i][0] + stations[i][1] < C:
            return "impossible"
    return "possible"

if __name__ == "__main__":
    C, n = map(int, sys.stdin.readline().split())
    stations = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
    print(possible(C, n, stations))
