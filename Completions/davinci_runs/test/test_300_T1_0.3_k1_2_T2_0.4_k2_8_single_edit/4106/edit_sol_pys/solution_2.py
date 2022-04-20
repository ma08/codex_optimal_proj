
n, k, x = map(int, input().split())
a = list(map(int, input().split()))

for i in range(1, k + 1):
    dp[i][0] = sum(a[:i])

dp = [[0] * (x + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, x + 1):
        if j < k:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - k][j - k] + sum(a[i - k:i]))

print(dp[n][x])
