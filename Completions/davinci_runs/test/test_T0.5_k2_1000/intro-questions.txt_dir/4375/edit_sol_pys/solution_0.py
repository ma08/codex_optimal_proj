
"""
This is a tree problem.

There are 2 cases:
1. If we choose the root, then we can only choose the subtrees of the root, and the root can't be in the subtrees.
2. If we don't choose the root, then we can choose the root and the subtrees of the root.

So the recurrence is:
dp[root][0] = max(dp[child][0] + dp[child][1] for child in children)
dp[root][1] = max(dp[child][0] for child in children)
"""

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
