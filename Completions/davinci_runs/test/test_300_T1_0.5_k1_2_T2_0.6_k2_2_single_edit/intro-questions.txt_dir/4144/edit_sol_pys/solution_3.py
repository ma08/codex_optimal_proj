# ---- answer ----

n = int(input())

dp = [[0]*2 for i in range(n+1)]
dp[0][0] = dp[0][1] = 1
mod = 10**9 + 7

for i in range(1, n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1])*3 % mod
    dp[i][1] = dp[i-1][0]*2 % mod

print(dp[n][0] + dp[n][1])
