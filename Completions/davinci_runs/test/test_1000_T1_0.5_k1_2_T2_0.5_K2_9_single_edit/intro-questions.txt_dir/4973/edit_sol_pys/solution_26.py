

import sys
sys.setrecursionlimit(1000000)
# Function to check if the move is valid
def isValid(i, j, N):
    if i >= 1 and i <= N and j >= 1 and j <= N:
        return True
    return False

# Function to find the minimum number of steps needed to reach the cell (1, 1)
def findMinSteps(i, j, N, board, dp):
    if i == 1 and j == 1:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    if board[i][j] == '#':
        return sys.maxsize

    x = sys.maxsize
    if isValid(i-2, j-1, N):
        x = min(x, findMinSteps(i-2, j-1, N, board, dp))
    if isValid(i-2, j+1, N):
        x = min(x, findMinSteps(i-2, j+1, N, board, dp))
    if isValid(i+2, j-1, N):
        x = min(x, findMinSteps(i+2, j-1, N, board, dp))
    if isValid(i+2, j+1, N):
        x = min(x, findMinSteps(i+2, j+1, N, board, dp))
    if isValid(i-1, j-2, N):
        x = min(x, findMinSteps(i-1, j-2, N, board, dp))
    if isValid(i-1, j+2, N):
        x = min(x, findMinSteps(i-1, j+2, N, board, dp))
    if isValid(i+1, j-2, N):
        x = min(x, findMinSteps(i+1, j-2, N, board, dp))
    if isValid(i+1, j+2, N):
        x = min(x, findMinSteps(i+1, j+2, N, board, dp))
    dp[i][j] = 1 + x
    return dp[i][j]

def main():
    N = int(input())
    board = []
    for i in range(N):
        board.append(input())
    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i-1][j-1] == 'K':
                x = findMinSteps(i, j, N, board, dp)
                if x == sys.maxsize:
                    print(-1)
                else:
                    print(x)
main()
