
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(h)] for _ in range(n)]

dp[0][a[0]] = 1
for i in range(1, n):
    for j in range(h):
        if j - a[i] >= 0 and j - a[i] + 1 < h:
            dp[i][j] = max(dp[i - 1][j - a[i]], dp[i - 1][j - a[i] + 1]) + (j >= l and j <= r)
        else:
            dp[i][j] = dp[i - 1][j - a[i] + 1] + (j >= l and j <= r)

ans = 0
for i in range(l, r + 1):
    ans = max(ans, dp[n - 1][i])

print(ans)
