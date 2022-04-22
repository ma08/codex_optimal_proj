

import sys

N, M = map(int, sys.stdin.readline().split())

board = [[0] * M for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, sys.stdin.readline().split()))

print(board)
