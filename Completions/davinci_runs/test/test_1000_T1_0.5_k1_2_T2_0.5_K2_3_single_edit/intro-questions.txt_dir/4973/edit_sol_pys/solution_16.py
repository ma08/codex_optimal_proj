

import sys
sys.setrecursionlimit(10000000)

# Function to check if the move is valid
def isValid(i, j, N):
    if i >= 0 and i < N and j >= 0 and j < N:
        return True
    return False

# Function to find the minimum number of steps needed to reach the cell (1, 1)
def findMinSteps(i, j, N, board, dp):
    if i == 0 and j == 0:
    if board[i][j] == '#':
        return sys.maxsize
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    x = sys.maxsize
    for i1 in range(i-2, i+3):
        for j1 in range(j-2, j+3):
            if isValid(i1, j1, N):
                x = min(x, findMinSteps(i1, j1, N, board, dp))

    dp[i][j] = 1 + x
    return dp[i][j]

def main():
    N = int(input())
    board = []
    for i in range(N):
        board.append(input())
    dp = [[-1 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'K':
                x = findMinSteps(i, j, N, board, dp)
                if x == sys.maxsize:
                    print(-1)
                else:
                    print(x)

main()
