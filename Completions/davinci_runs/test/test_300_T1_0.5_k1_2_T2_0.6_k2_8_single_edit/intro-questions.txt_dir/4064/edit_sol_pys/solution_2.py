# https://atcoder.jp/contests/dp/tasks/dp_b

import sys

N, K = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][(j-h[i-1]+K)%K])
        if j-h[i-1] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-h[i-1]]+1)
        else:
            dp[i][j] = max(dp[i][j], dp[i-1][j-h[i-1]+K]+1)
print(max(dp[N]))
