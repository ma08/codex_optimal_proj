
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)


def dfs(i, used):
    if used == (1 << n) - 1:
        return 1
    res = 0
    for j in edges[i]:
        if used >> j & 1 == 1:
            continue
        res += dfs(j, used | (1 << j))
    return res


print(dfs(0, 1))
