
import sys
from collections import deque

# read the input
N = int(sys.stdin.readline())
board = []
for i in range(N):
    board.append(list(sys.stdin.readline().strip()))

start = (-1, -1)
# find the starting point of the knight.
for i in range(N):
    for j in range(N):
        if board[i][j] == "K":
            start = (i, j)
            break
