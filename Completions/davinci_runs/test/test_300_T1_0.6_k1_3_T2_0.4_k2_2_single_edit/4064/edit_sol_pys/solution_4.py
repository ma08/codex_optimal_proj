
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0 for _ in range(h)] for _ in range(n + 1)]

dp[0][0] = 1
for i in range(1, n):
    for j in range(h + 1):
        dp[i][j] = max(dp[i - 1][j - a[i]] + (l <= j - a[i] <= r), dp[i - 1][j - a[i] + 1] + (l <= j - a[i] + 1 <= r))

print(max(dp[n]))
