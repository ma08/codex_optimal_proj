
n, h, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * h for _ in range(n)]
dp[0][0] = 1
for i in range(1, h):
    dp[0][i] = dp[0][i-1]
    if i >= a[0]:
        dp[0][i] = max(dp[0][i], dp[0][i-a[0]])
for i in range(1, n):
    dp[i][0] = 1
    for j in range(1, h):
        dp[i][j] = dp[i][j-1]
        if j >= a[i]:
            dp[i][j] = max(dp[i][j], dp[i][j-a[i]])
        if j >= a[i] - 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j-a[i]+1])

print(sum(dp[n-1][l:r+1]))
