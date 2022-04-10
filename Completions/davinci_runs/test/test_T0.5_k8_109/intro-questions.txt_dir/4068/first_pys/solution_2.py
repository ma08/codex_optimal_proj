

import sys

N, M = map(int, sys.stdin.readline().split())
broken = [int(sys.stdin.readline()) for i in range(M)]

# dp[i] = i番目までのステップを登った時の登り方の総数
dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, N+1):
    if i in broken:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 1000000007)