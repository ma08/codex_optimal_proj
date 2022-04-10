n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n)
for i in range(n - 1):
    dp[i + 1] = dp[i] + a[i + 1]

best = 0
for i in range(n - k):
    best = max(best, dp[i + k] - dp[i])

for i in range(n - k - x + 1):
    best = max(best, dp[i + k + x] - dp[i])

print(best)
