

n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

# dp[i][j] = maximum number of good times Vova can obtain by sleeping n times,
# where the last time he slept is at time j
dp = [[0 for _ in range(h)] for _ in range(n)]

dp[0][a[0] % h] = 1

for i in range(1, n):
    for j in range(h):
        # Vova can't sleep at time j, so he has to sleep at time j-1
        if j == 0:
            dp[i][j] = dp[i - 1][h - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1]

        # Vova can sleep at time j, so he has to sleep at time j-a[i]
        if l <= j < r:
            dp[i][j] += 1
        if j - a[i] < 0:
            dp[i][j] += dp[i - 1][j - a[i] + h]
        else:
            dp[i][j] += dp[i - 1][j - a[i]]

print(max(dp[n - 1]))