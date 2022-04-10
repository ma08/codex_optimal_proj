

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

# dp[i] = the maximum number of good sleeping times Vova can obtain if he acts optimally
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    dp[i] = max(dp[i + 1], dp[i + 1] + (l <= (a[i] - 1) % h <= r))
print(dp[0])