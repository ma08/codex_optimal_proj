

import sys, heapq
sys.setrecursionlimit(10**8)

N, M = map(int, input().split())

adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)

# def dfs(v, visited):
#     visited.add(v)
#     for child in adj[v]:
#         if child not in visited:
#             dfs(child, visited)

# visited = set()
# dfs(0, visited)

# if len(visited) != N:
#     print(0)
#     sys.exit()

# ans = 1
# for i in range(N):
#     if i == 0:
#         continue
#     if len(adj[i]) > 1:
#         ans *= len(adj[i])
