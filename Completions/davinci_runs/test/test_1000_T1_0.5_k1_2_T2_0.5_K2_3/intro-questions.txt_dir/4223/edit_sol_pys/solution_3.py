
from collections import Counter, deque

n = int(input()) # number of nodes
m = int(input()) # number of edges

visited = [False] * n
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(v):
    visited[v] = True
    print(v + 1)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    visited[v] = True
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        print(v + 1)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


bfs(0)
