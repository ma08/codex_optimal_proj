
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

G = [[] for _ in range(N)]
for a, b in AB:
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def bfs(start):
    q = deque([start])
    d = [-1] * N
    d[start] = 0
    while q:
        v = q.popleft()
        for u in G[v]:
            if d[u] != -1:
                continue
            else:
                d[u] = d[v] + 1
                q.append(u)
    return d


d = bfs(0)
ans = 0
for i in range(N):
    if d[i] == 2:
        ans += 1
print(ans)
