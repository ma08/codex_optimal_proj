

n, m = map(int, input().split())
coins = [int(input()) for _ in range(m)]

dp = [0] * (n + 1)
dp[0] = 1 # 정답이 1개 나올 수 있다.

for coin in coins:
    for i in range(coin, n+1):
        dp[i] += dp[i - coin]

print(dp[n])
