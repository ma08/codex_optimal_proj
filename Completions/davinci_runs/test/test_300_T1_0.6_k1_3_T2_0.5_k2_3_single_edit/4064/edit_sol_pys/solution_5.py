
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(h)] for _ in range(n)]

dp[0][a[0]] = 1
for i in range(1, n):
    for j in range(h):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][(j - a[i] + h) % h])

ans = 0
for i in range(l, r + 1):
    ans = max(ans, dp[n - 1][i])

print(ans)
