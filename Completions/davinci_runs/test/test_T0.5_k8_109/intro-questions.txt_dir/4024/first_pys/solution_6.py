

from collections import defaultdict
from sys import stdin
from itertools import product
from functools import lru_cache
from heapq import heappush, heappop


def solve(s, k):
    n = len(s)
    d = defaultdict(list)
    for i in range(n):
        d[s[i]].append(i)
    d = list(d.values())
    d.sort(key=len)
    d = [tuple(x) for x in d]
    @lru_cache(maxsize=None)
    def f(i, j, x):
        if j == 0:
            return 0
        if i == n:
            return float('inf')
        if x == 0:
            return float('inf')

        best = float('inf')
        for y in range(len(d[i])):
            if d[i][y] >= j:
                best = min(best, f(i + 1, d[i][y], x - 1) + d[i][y] - j)
            else:
                best = min(best, f(i + 1, d[i][y], x - 1) + d[i][y] + n - j)
        return best
    best = float('inf')
    for x in range(n):
        best = min(best, f(0, x, k))
    if best == float('inf'):
        return -1
    return best


def main():
    n, k = map(int, stdin.readline().split())
    s = stdin.readline()
    print(solve(s, k))


if __name__ == '__main__':
    main()