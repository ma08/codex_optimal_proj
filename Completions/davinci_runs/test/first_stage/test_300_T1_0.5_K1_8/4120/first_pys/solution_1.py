

import sys
sys.setrecursionlimit(2 * 10 ** 5)

n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * n

def dfs(v):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

dfs(0)

if any(not visited):
    print(0)
    exit()

def dfs_for_dist(v, dist):
    visited[v] = True
    for w in graph[v]:
        if not visited[w]:
            dfs_for_dist(w, dist + 1)

visited = [False] * n
dfs_for_dist(0, 0)

if any(not visited):
    print(0)
    exit()

visited = [False] * n

def dfs_for_k(v, dist, k):
    visited[v] = True
    if dist > k:
        return
    if dist == k:
        if all(visited):
            print(1)
            print('1' * m)
            exit()
        return

    for w in graph[v]:
        if not visited[w]:
            dfs_for_k(w, dist + 1, k)

dfs_for_k(0, 0, k)

print(0)