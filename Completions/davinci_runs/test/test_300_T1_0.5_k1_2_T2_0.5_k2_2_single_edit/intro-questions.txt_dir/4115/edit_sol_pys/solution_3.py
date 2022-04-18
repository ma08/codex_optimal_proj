

import sys
sys.setrecursionlimit(1000000)

def dfs(i, j):
    if i == n or j == n:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if s[i] == t[j]:
        dp[i][j] = dfs(i + 1, j + 1) + 1
    else:
        dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))
    return dp[i][j]

n = int(input())
s = input()
t = input()

dp = [[-1] * n for _ in range(n)]

print(n - dfs(0, 0))

s = input()
