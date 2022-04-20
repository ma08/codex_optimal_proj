import sys
input = sys.stdin.readline


n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]    
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
dp[0][0] = 1
for i in range(1, n+1):
    for j in range(k+1):
        dp[i][j] = dp[i-1][j]
        if j - a[i-1] >= 0:
            dp[i][j] += dp[i-1][j-a[i-1]]

print(dp[n][k])
