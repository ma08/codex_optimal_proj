

import sys

N = int(input())

ans = 0

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            ans += gcd(gcd(i, j),k)

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
