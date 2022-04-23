

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(h)] for _ in range(n)]
dp[0][0] = 1 if l <= 0 <= r else 0
for i in range(1, n):
    for j in range(h):
        dp[i][j] = max(dp[i - 1][(j - a[i] + h) % h], dp[i - 1][(j - a[i] + 1 + h) % h])

ans = 0
for i in range(h):
    if l <= i <= r:
        ans += dp[n - 1][i]

print(ans)
