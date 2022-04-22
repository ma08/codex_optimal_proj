

import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))


def solve():
    N, M = inm()
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = inm()
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    q = deque()
    q.append(0)
    visited = set()
    visited.add(0)
    while q:
        u = q.popleft()
        for v in G[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return len(visited) == N


print("Yes" if solve() else "No")
