

from collections import deque

n = int(input())

edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)

c = list(map(int, input().split()))

c.sort()
c.reverse()

color = [-1 for _ in range(n)]


def dfs(v, p):
    color[v] = c.pop()

    for u in edges[v]:
        if u == p:
            continue
        dfs(u, v)


dfs(0, -1)

print(sum(color))
print(*color)
