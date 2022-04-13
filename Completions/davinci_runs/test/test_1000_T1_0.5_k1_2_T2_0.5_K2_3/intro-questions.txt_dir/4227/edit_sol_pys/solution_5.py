

import sys, collections
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

graph = collections.defaultdict(set)
for _ in range(M):
    a, b = map(int, input().split()) # 1-indexed
    graph[a-1].add(b-1)
    graph[b-1].add(a-1)

def dfs(v, visited, graph):
    visited[v] = True
    for child in graph[v]:
        if visited[child]:
            continue
        dfs(child, visited, graph)

visited = [False] * N
dfs(0, visited, graph)

if not all(visited):
    print(0)
    sys.exit()

ans = 1
for i in range(N):
    if i == 0:
        continue
    if len(graph[i]) > 1:
        ans *= len(graph[i])

print(ans)
