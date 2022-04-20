
import sys

N, M = map(int, input().split())

tree = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# DFS

def dfs(v, visited):
    visited.add(v)
    for child in tree[v]:
        if child not in visited:
            dfs(child, visited)



def bfs(v, visited):
    queue = [v]
    visited.add(v)
    while queue:
        v = queue.pop(0)
        for child in tree[v]:
            if child not in visited:
                queue.append(child)
                visited.add(child)


visited = set()  # 集合で管理することで、重複を防ぐ
dfs(1, visited)
# bfs(1, visited)

if len(visited) != N:
    print(0)
    sys.exit()

ans = 1
for i in range(N):
    if i == 1:
        continue
    if len(tree[i]) > 1:
        ans *= len(tree[i])

ans %= 10**9+7
print(ans)
