

import math
n, m = map(int, input().split())
k = int(input())
a = [list(map(int, input().split())) for i in range(n)]

dp = [[[0 for i in range(k+1)] for i in range(m+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j >= m//2:
            for t in range(k+1):
                dp[i][j][t] = max(dp[i-1][j][t], dp[i-1][j-1][t] + a[i-1][j-1])
        else:
            for t in range(k+1):
                dp[i][j][t] = dp[i-1][j][t]

print(dp[n][m])
