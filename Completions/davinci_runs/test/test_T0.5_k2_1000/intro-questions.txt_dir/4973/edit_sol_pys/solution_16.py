

import sys
sys.setrecursionlimit(1000000)
import math
# Function to check if the move is valid.
def isValid(i, j, N):
    if i >= 0 and i < N and j >= 0 and j < N:
        return True
    return False

# Function to find the minimum number of steps needed to reach the cell (1, 1).
def findMinSteps(i, j, N, board, dp):
    if i == 0 and j == 0:
        return 0

    if dp[i][j] != math.inf:
        return dp[i][j]

    if board[i][j] == '#':
        return sys.maxsize

    x = math.inf
    if isValid(i-2, j-1, N) and board[i-2][j-1] != '#':
        x = min(x, 1 + findMinSteps(i-2, j-1, N, board, dp))
    if isValid(i-2, j+1, N) and board[i-2][j+1] != '#':
        x = min(x, 1 + findMinSteps(i-2, j+1, N, board, dp))
    if isValid(i+2, j-1, N) and board[i+2][j-1] != '#':
        x = min(x, 1 + findMinSteps(i+2, j-1, N, board, dp))
    if isValid(i+2, j+1, N) and board[i+2][j+1] != '#':
        x = min(x, 1 + findMinSteps(i+2, j+1, N, board, dp))
    if isValid(i-1, j-2, N) and board[i-1][j-2] != '#':
        x = min(x, 1 + findMinSteps(i-1, j-2, N, board, dp))
    if isValid(i-1, j+2, N) and board[i-1][j+2] != '#':
        x = min(x, 1 + findMinSteps(i-1, j+2, N, board, dp))
    if isValid(i+1, j-2, N) and board[i+1][j-2] != '#':
        x = min(x, 1 + findMinSteps(i+1, j-2, N, board, dp))
    if isValid(i+1, j+2, N) and board[i+1][j+2] != '#':
        x = min(x, 1 + findMinSteps(i+1, j+2, N, board, dp))

    dp[i][j] = x
    return dp[i][j]

def main():
    N = int(input())
    board = []
    for i in range(N):
        board.append(input())
    dp = [[math.inf for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'K':
                x = findMinSteps(i, j, N, board, dp)
                if x == math.inf:
                    print(-1)
                else:
                    print(x)

main()
