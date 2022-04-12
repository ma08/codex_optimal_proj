# https://atcoder.jp/contests/dp/tasks/dp_g

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)


def dfs(v, p):
    for u in edges[v]:
        if u == p:
            continue
        dfs(u, v)
        dp[v] += dp[u]


dp = [1] * n
dfs(0, -1)
print(dp[0])
