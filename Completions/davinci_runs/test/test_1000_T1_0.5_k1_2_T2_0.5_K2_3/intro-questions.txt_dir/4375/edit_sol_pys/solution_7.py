

import sys
sys.setrecursionlimit(10**6)

def dfs(root):
    dp[root][0] = 0
    dp[root][1] = 0
    for child in graph[root]:
        dfs(child)
        dp[root][0] += max(dp[child][0], dp[child][1])
        dp[root][1] += dp[child][0]

n, k = map(int, input().split())
a = list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)

dp = [[0, 0] for _ in range(n + 1)]
dfs(1)

ans = max(dp[1][0], dp[1][1])
print(ans)
