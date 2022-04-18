

# Solved by: Raul Gonzalez, Anirudh
# Date: 4/12/2020
# Time: 12:40pm, 12:55pm

def check_valid(board, N):
    for row in range(N):
        for col in range(N):
            for i in range(N):
                if (board[row][col] == board[row][i] or board[row][col] == board[i][col]):
                    return False
                elif (board[row][col] == board[row - i][col - i] or board[row][col] == board[row + i][col - i]):
                    return False
                elif (board[row][col] == board[row - i][col + i] or board[row][col] == board[row + i][col + i]):
                    return False
    return True

N = int(input())
board = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    x, y = input().split()
    board[int(x)][int(y)] = 1

if (check_valid(board, N)):
    print("CORRECT")
else:
    print("INCORRECT")
