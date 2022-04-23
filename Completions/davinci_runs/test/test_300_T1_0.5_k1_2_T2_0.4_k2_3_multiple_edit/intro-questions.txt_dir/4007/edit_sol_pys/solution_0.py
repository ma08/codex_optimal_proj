
from collections import deque
n, m = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n
dist = [float('inf')] * n
dist[0] = 0

q = deque([0])
while q:
    v = q.popleft()
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dist[u] = dist[v] + 1
            q.append(u)

print(*dist)
