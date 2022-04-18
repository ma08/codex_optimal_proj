

n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

for i in range(n):
    dp[i + 1] = max(dp[i], dp[i] + a[i])

print(max(dp))
