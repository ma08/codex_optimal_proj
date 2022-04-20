

# Solution

import sys

def dfs(adj, visited, v):
    visited[v] = True
    for u in adj[v]:
        if not visited[u]:
            dfs(adj, visited, u)

n, m, s = [int(x) for x in sys.stdin.readline().split()]
adj = [[] for _ in range(n)]
for _ in range(m):
    u, v = [int(x) for x in sys.stdin.readline().split()]
    adj[u - 1].append(v - 1)

visited = [False] * n
dfs(adj, visited, s - 1)

not_visited = [i for i in range(n) if not visited[i]]

print(len(not_visited))