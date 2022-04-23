
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(h)] for _ in range(n + 1)]

for i in range(n):
    for j in range(h + 1):
        dp[i + 1][(j + a[i]) % h] = max(dp[i + 1][(j + a[i]) % h], dp[i][j] + (l <= (j + a[i]) % h <= r))
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])

print(max(dp[n]))
