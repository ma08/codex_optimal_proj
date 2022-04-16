

import sys
sys.stdin = open('input.txt', 'r')

board = []
for i in range(8):
    board.append(list(input()))

white = []
black = []

for i in range(8):
    for j in range(8):
        if board[i][j] == 'K':
            white.append('Ke1')
        if board[i][j] == 'Q':
            white.append('Qd1')
        if board[i][j] == 'R':
            white.append('Ra1')
        if board[i][j] == 'B':
            white.append('Bc1')
        if board[i][j] == 'N':
            white.append('Nb1')
        if board[i][j] == 'P':
            white.append('a2')
        if board[i][j] == 'k':
            black.append('Ke8')
        if board[i][j] == 'q':
            black.append('Qd8')
        if board[i][j] == 'r':
            black.append('Ra8')
        if board[i][j] == 'b':
            black.append('Bc8')
        if board[i][j] == 'n':
            black.append('Ng8')
        if board[i][j] == 'p':
            black.append('a7')

print('White:', ','.join(white))
print('Black:', ','.join(black))
