

# Date: 4/19/2020
# Time: 11:08am

def check_valid(board, N, row, col):
    for i in range(N):
        if (col != i):
            if (board[row][col] == board[row][i]):
                return False
        if (row != i):
            if (board[row][col] == board[i][col]):
                return False
        if (row - i >= 0):
            if (col - i >= 0):
                if (board[row][col] == board[row - i][col - i]):
                    return False
            if (col + i < N):
                if (board[row][col] == board[row - i][col + i]):
                    return False
        if (row + i < N):
            if (col - i >= 0):
                if (board[row][col] == board[row + i][col - i]):
                    return False
            if (col + i < N):
                if (board[row][col] == board[row + i][col + i]):
                    return False
    return False

N = int(input())
board = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    x, y = input().split()
    board[int(x)][int(y)] = "Q"

if (check_valid(board, N, row, col)):
    print("CORRECT")
else:
    print("INCORRECT")
