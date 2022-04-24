import sys
sys.setrecursionlimit(10000000)
n, m, k = map(int, input().split())
k -= 1
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[0 for i in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0:
            dp[i][j] = a[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + a[i][j]
        elif j == m-1:
            dp[i][j] = dp[i-1][j-1] + a[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]

def dfs(i, j):
    if i == n-1:
        return dp[i][j]

print(dp[n][m])
