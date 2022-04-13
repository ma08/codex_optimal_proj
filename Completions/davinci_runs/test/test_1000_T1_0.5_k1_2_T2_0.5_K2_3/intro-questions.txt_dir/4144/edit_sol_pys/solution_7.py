n = int(input())


dp = [[0]*2 for _ in range(n)]
dp[0][0] = 1
mod = 10**9+7

for i in range(1,n+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1]) % mod
    dp[i][1] = dp[i-1][0]

print((dp[n][0] + dp[n][1]) % mod)
