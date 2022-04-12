
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue

        if board[i][j] == 0:
            continue

        if i-1 >= 0:
            dp[i][j] += dp[i-1][j]
        if j-1 >= 0:
            dp[i][j] += dp[i][j-1]

print(dp[n-1][m-1])
