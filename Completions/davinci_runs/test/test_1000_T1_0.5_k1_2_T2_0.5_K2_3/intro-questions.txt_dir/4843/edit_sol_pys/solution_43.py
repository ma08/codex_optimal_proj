

# Solved by: Raul Gonzalez
# Date: 4/13/2020
# Time: 11:09am

def is_valid(board, N):
    for row in range(len(board)):
        for col in range(len(board)):
            for i in range(len(board)):
                if (row != i and col != i and board[row][col] == board[row][i]):
                    return False
                elif (row != i and col != i and board[row][col] == board[i][col]):
                    return False
                elif (row != i and col != i and board[row][col] == board[row - i][col - i]):
                    return False
                elif (row != i and col != i and board[row][col] == board[row + i][col - i]):
                    return False
                elif (row != i and col != i and board[row][col] == board[row - i][col + i]):
                    return False
                elif (row != i and col != i and board[row][col] == board[row + i][col + i]):
                    return False
    return False

n = int(input())
board = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    x, y = input().split()
    board[int(x)][int(y)] = 1

if (is_valid(board, n)):
    print("CORRECT")
else:
    print("INCORRECT")
