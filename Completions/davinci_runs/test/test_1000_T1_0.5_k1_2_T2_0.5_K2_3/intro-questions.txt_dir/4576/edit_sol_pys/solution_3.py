
# coding: utf-8
"""
    动态规划
    dp[i][j]表示总金额为i，硬币种类为j的组合数，dp[i][j] = dp[i-500][j] + dp[i-100][j] + dp[i-50][j-1]
    dp[i][0] = 1
    dp[0][i] = 0
"""

A, B, C, X = map(int, input().split())
dp = [[0 for _ in range(C+1)] for _ in range(X+1)]

for i in range(C+1):
    dp[0][i] = 1

print(dp[X][C])
