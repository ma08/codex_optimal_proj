
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    for j in range(i - 1, -1, -1):
        if a[i - 1] - a[j] <= 5:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0
for i in range(n, n - k, -1):
    ans = max(ans, dp[i])
print(ans)
