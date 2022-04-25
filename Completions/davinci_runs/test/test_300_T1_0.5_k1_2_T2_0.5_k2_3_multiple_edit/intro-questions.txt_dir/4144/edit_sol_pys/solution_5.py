import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

N = int(input())
MOD = 10**9 + 7

graph = [[] for _ in range(N)]


for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)


def bfs(graph, start):
    queue = deque([[start, 0]])
    dist = [-1] * N
    while queue:
        v, d = queue.popleft()
        if dist[v] != -1:
            continue
        dist[v] = d
        for nv in graph[v]:
            if dist[nv] == -1:
                queue.append([nv, d + 1])
    return dist


dist = bfs(graph, 0)

res = 0
for i in range(N):
    res += dist[i]

print(res)
