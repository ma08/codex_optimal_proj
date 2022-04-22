

import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

tree = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

def dfs(v, visited):
    visited.add(v)
    for child in tree[v]:
        if child not in visited:
            dfs(child, visited)

visited = set()
dfs(0, visited)

if len(visited) != N:
    print(0)
    exit()

ans = 1
for i in range(N):
    if i == 0:
        continue
    if len(tree[i]) > 1:
        ans *= len(tree[i])

print(ans)
