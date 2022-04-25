import sys

N, M = map(int, input().split())

tree = [set() for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a-1].add(b-1)
    tree[b-1].add(a-1)

def dfs(v):
    visited = set()
    stack = [v]
    while stack:
        v = stack.pop()
        if v in visited:
            continue
        visited.add(v)
        stack.extend(tree[v])
    return visited

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
