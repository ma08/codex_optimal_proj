

# Solved by: Raul Gonzalez
# Date: 4/12/2020
# Time: 12:40pm

def check_valid(board, N):
    for row in range(N - 1):
        for col in range(N - 1):
            if (board[row][col] == board[row][col + 1] or board[row][col] == board[row + 1][col]):
                return False
            elif (board[row][col] == board[row - 1][col - 1] or board[row][col] == board[row + 1][col - 1]):
                return False
            elif (board[row][col] == board[row - 1][col + 1] or board[row][col] == board[row + 1][col + 1]):
                return False
    return True

def main():
    N = int(input())
    board = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        x, y = input().split()
        board[int(x)][int(y)] = 1

    if (check_valid(board, N)):
        print("CORRECT")
    else:
        print("INCORRECT")

if __name__ == "__main__":
    main()
