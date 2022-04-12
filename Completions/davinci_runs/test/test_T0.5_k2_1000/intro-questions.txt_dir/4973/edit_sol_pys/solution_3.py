
import sys
sys.setrecursionlimit(1000000)

def isValid(i, j, N):
    if i >= 1 and i <= N and j >= 1 and j <= N:
        return True
    return False

def findMinSteps(i, j, N, board, dp):
    if i == 1 and j == 1: #if the knight is at the bottom left corner
        return 0

    if dp[i][j] != -1: #if the knight is at a cell that has already been visited
        return dp[i][j]

    if board[i][j] == '#': #if the knight is at a cell that has a block
        return sys.maxsize

    x = sys.maxsize #initialize x to infinity
    #check if the knight can move to any of the 8 cells
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

    dp[i][j] = 1 + x #set the value of the cell to 1 + the minimum value of the 8 cells
    return dp[i][j]

def main():
    #input the dimensions of the board
    N = int(input())
    #input the board
    board = []
    for i in range(N):
        board.append(input())
    #initialize the dp array
    dp = [[-1 for i in range(N+1)] for j in range(N+1)]
    #find the minimum number of steps needed to reach the cell (1, 1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i-1][j-1] == 'K': #if the knight is at the cell
                x = findMinSteps(i, j, N, board, dp)
                if x == sys.maxsize:
                    print(-1)
                else:
                    print(x)

main()
