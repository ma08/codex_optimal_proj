import sys
sys.setrecursionlimit(10**9)

n,h,l,r = map(int, input().split()) # n,h,l,rの入力
a = list(map(int, input().split())) # aの入力

dp = [[[-1 for _ in range(h)] for _ in range(n+1)] for _ in range(n+1)]
def dfs(i, j, k):
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    if i == n:
        return 0
    else:
        if l <= (k+a[i])%h <= r:
            dp[i][j][k] = max(dfs(i+1, j+1, (k+a[i])%h), dfs(i+1, j, k))+1
        else:
            dp[i][j][k] = max(dfs(i+1, j+1, (k+a[i])%h), dfs(i+1, j, k))
        return dp[i][j][k]

print(dfs(0, 0, 0))
