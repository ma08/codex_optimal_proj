

import sys, heapq

def dfs(v, visited):
    visited.add(v)
    for nv in tree[v]:
        if nv not in visited:
            dfs(nv, visited)
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

tree = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) # 0-indexed
    tree[a].append(b)
    tree[b].append(a)

# print(tree)

visited = set()
dfs(0, visited)

if len(visited) != N:
    print(0)
    sys.exit()

ans = 1
for i in range(N):
    if i == 0:
        continue
    if len(tree[i]) > 1:
        ans *= len(tree[i])

print(ans)
