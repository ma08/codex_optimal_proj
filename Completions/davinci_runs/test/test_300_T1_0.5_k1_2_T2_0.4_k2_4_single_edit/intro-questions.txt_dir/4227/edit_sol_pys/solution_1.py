
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)


def dfs(v, p):
    for to in edges[v]:
        if to == p:
            continue
        dfs(to, v)
        # TODO:
        # ここに処理を書く


dfs(0, -1)
print(0)
