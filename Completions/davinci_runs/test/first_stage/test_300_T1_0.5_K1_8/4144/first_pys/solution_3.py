
# N = int(input())

N = 2

mod = 10**9 + 7

dp = [[0]*10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(10):
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= mod

ans = 0
for i in range(10):
    ans += dp[N][i]
    ans %= mod

print(ans)