

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(n):
    dp[i + 1] = dp[i] + a[i]

best = 0
for i in range(k):
    best = max(best, dp[n - i])

for i in range(k, n - x + 1):
    best = max(best, dp[i + x] - dp[i])

print(best)