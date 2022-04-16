

import sys
sys.setrecursionlimit(1000000)
n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False] * n

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(graph, node, visited):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(graph, i, visited)

k = 0
for i in range(n):
    if not visited[i]:
        dfs(graph, i, visited)
        k += 1
print(k)
