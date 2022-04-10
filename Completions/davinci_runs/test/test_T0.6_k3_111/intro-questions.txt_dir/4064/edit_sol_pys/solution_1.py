n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * 2 for _ in range(n)]
dp[0][0] = dp[0][1] = 0
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + (l <= (a[i - 1] + a[i]) % h < r)
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) + (l <= (a[i - 1] + a[i] - 1) % h < r)

print(max(dp[-1]))
