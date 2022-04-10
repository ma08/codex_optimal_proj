

n, h, l, r = list(map(int, input().split()))
a = list(map(int, input().split()))

dp = [[0, 0] for i in range(n)]

dp[0][0] = 1 if l <= a[0] <= r else 0
dp[0][1] = 1 if l <= a[0] - 1 <= r else 0

for i in range(1, n):
    if a[i] - a[i - 1] <= 1:
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = dp[i][0]
    else:
        dp[i][0] = dp[i - 1][0] + 1 if l <= a[i] <= r else dp[i - 1][0]
        dp[i][1] = dp[i - 1][1] + 1 if l <= a[i] - 1 <= r else dp[i - 1][1]

print(max(dp[n - 1][0], dp[n - 1][1]))