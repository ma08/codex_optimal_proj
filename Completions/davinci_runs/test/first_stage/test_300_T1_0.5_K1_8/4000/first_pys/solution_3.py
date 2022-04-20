

import sys

sys.setrecursionlimit(10**6)

def dfs(v, p):
    for u in g[v]:
        if u != p:
            dfs(u, v)
            if dp[u] > 0:
                dp[v] += dp[u]
                if dp[u] > 1:
                    dp[v] += 1
                if dp[v] > res[0]:
                    res[0] = dp[v]
                    res[1] = v
                    res[2] = u
                    res[3] = -1
                elif dp[v] == res[0] and res[3] == -1:
                    res[3] = u

n = int(input())
g = [[] for i in range(n + 1)]
dp = [0] * (n + 1)
res = [0, 0, 0, -1]

for i in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

dfs(1, -1)

print(res[0])
print(res[1], res[3], res[2])