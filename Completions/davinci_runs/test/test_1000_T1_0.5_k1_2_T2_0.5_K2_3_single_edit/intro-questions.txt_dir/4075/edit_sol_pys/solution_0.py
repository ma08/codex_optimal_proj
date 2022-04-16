

from collections import deque

N, M = map(int, input().split())

def bfs(n, m, graph, start, goal):
    q = deque([start])
    visited = [False] * (n+1)
    visited[start] = True
    while q:
        v = q.popleft()
        if v == goal:
            return visited.count(True) - 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return -1

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(N, M, graph, 1, N))
