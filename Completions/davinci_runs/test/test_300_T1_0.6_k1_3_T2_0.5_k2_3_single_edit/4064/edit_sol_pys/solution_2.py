
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0, 0] for i in range(n)]

if a[0] > l and a[0] < r:
    dp[0][0] = 1
else:
    dp[0][0] = 0
if a[0] - 1 > l and a[0] - 1 < r:
    dp[0][1] = 1
else:
    dp[0][1] = 0

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
    if a[i] > l and a[i] < r:
        dp[i][0] += 1
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
    if a[i] - 1 > l and a[i] - 1 < r:
        dp[i][1] += 1

print(max(dp[n - 1][0], dp[n - 1][1]))
