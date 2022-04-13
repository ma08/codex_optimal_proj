
import sys
sys.setrecursionlimit(1000000)

def isValid(i, j, N):
    if i >= 0 and i < N and j >= 0 and j < N:
        return True
    return False


def findMinSteps(i, j, N, board, dp):
    if i == 0 and j == 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    if board[i][j] == '#':
        return sys.maxsize

    x = sys.maxsize
    if isValid(i-2, j-1, N) and board[i-2][j-1] != '#':
        x = min(x, findMinSteps(i-2, j-1, N, board, dp) + 1)
    if isValid(i-2, j+1, N) and board[i-2][j+1] != '#':
        x = min(x, findMinSteps(i-2, j+1, N, board, dp) + 1)
    if isValid(i+2, j-1, N) and board[i+2][j-1] != '#':
        x = min(x, findMinSteps(i+2, j-1, N, board, dp) + 1)
    if isValid(i+2, j+1, N) and board[i+2][j+1] != '#':
        x = min(x, findMinSteps(i+2, j+1, N, board, dp) + 1)
    if isValid(i-1, j-2, N) and board[i-1][j-2] != '#':
        x = min(x, findMinSteps(i-1, j-2, N, board, dp) + 1)
    if isValid(i-1, j+2, N) and board[i-1][j+2] != '#':
        x = min(x, findMinSteps(i-1, j+2, N, board, dp) + 1)
    if isValid(i+1, j-2, N) and board[i+1][j-2] != '#':
        x = min(x, findMinSteps(i+1, j-2, N, board, dp) + 1)
    if isValid(i+1, j+2, N) and board[i+1][j+2] != '#':
        x = min(x, findMinSteps(i+1, j+2, N, board, dp) + 1)

    dp[i][j] = x
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
