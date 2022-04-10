

n, m = map(int, input().split())
broken = [int(input()) for i in range(m)]

# dp[i] = i番目の階段までの上り方
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    if i in broken:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 1000000007)