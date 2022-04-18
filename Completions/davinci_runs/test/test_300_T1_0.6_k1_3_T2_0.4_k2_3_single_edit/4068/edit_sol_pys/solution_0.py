# 백준 9465번 문제
# https://www.acmicpc.net/problem/9465

import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    sticker = []
    for j in range(2):
        sticker.append([int(x) for x in sys.stdin.readline().split()])

    dp = [[0 for _ in range(N)] for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    for j in range(1, N):
        dp[0][j] = max(dp[1][j-1], dp[1][j-2]) + sticker[0][j]
        dp[1][j] = max(dp[0][j-1], dp[0][j-2]) + sticker[1][j]

print(dp[N])
