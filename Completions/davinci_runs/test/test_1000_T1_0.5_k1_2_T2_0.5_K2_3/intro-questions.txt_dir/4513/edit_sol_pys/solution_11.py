

import math
import sys

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        board = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(9)]
        solve(board, 0)

def solve(board, pos):
    if pos == 81:
        for row in board:
            print(''.join(map(str, row)))
                return
    i = pos // 9
    j = pos % 9
    if board[i][j] == 0:
        for k in range(1, 10):
            if check(i, j, k, board):
                board[i][j] = k
                solve(board, pos+1)
                board[i][j] = 0
    else:
        solve(board, pos+1)

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
