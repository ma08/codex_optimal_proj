

n, m, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + a[i - 1][j - 1]

ans = 0
for i in range(1, n + 1):
    for j in range(0, min(m // 2 + 1, m)):
        ans = max(ans, dp[i][m] - dp[i][m - j] - dp[i][j])
print(ans)