
import sys
N, M = map(int, input().split())

tree = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

visited = set([0])
stack = [0]
while stack:
    v = stack.pop()
    for child in tree[v]:
        if child not in visited:
            visited.add(child)
            stack.append(child)

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
