# https://www.acmicpc.net/problem/15990

n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

dp = [[[0 for l in range(4)] for j in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j][1] = dp[i-1][j-1][2] + dp[i-1][j-1][3]
        dp[i][j][2] = dp[i-1][j-1][1] + dp[i-1][j-1][3]
        dp[i][j][3] = dp[i-1][j-1][1] + dp[i-1][j-1][2]

        if j >= 2:
            dp[i][j][1] += dp[i-1][j-2][2]
            dp[i][j][2] += dp[i-1][j-2][1]

        if j >= 3:
            dp[i][j][1] += dp[i-1][j-3][3]
            dp[i][j][3] += dp[i-1][j-3][1]

        dp[i][j][1] %= 1000000009
        dp[i][j][2] %= 1000000009
        dp[i][j][3] %= 1000000009

print((dp[n][m][1] + dp[n][m][2] + dp[n][m][3]) % 1000000009)
