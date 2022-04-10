

# Solution

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0]*(x+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, x+1):
        if i < j*k:
            dp[i][j] = -1
            continue
        if j == 1:
            dp[i][j] = sum(a[:i])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-k][j-1] + sum(a[i-k:i]))

print(dp[n][x])