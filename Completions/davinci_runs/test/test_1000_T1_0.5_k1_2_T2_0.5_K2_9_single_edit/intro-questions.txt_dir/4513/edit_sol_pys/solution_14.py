
import math
import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        board = [[0 for j in range(9)] for k in range(9)]
        for j in range(9):
            board[j] = list(map(int, list(sys.stdin.readline())))
        print("Case #" + str(i+1) + ":")
        solve(board)

def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for k in range(1, 10):
                    if check(i, j, k, board):
                        board[i][j] = k
                        solve(board)
                        board[i][j] = 0
                return
    for i in range(9):
        for j in range(9):
            print(str(board[i][j]), end = '')
        print()
    exit()

def check(i, j, val, board):
    for k in range(9):
        if board[i][k] == val:
            return False
    for k in range(9):
        if board[k][j] == val:
            return False
    x = i // 3
    y = j // 3
    for k in range(3):
        for l in range(3):
            if board[(x*3) + k][(y*3) + l] == val:
                return False
    return True

if __name__ == "__main__":
    main()
