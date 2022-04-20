

n, w = map(int, input().split())
a = list(map(int, input().split()))

# dp[i] is the number of ways to reach a[i]
dp = [0] * n
dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if dp[j] == 0:
            continue
        if a[i] - a[j] >= 0 and a[i] - a[j] <= w:
            dp[i] += dp[j]

print(dp[-1])