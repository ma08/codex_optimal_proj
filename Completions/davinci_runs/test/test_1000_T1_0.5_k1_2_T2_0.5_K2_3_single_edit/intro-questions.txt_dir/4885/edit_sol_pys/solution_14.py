

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
        elif board[i][j] == 'Q':
            white.append('Qd1')
        elif board[i][j] == 'R':
            white.append('Ra1')
        elif board[i][j] == 'b':
            white.append('Bc1')
        elif board[i][j] == 'n':
            white.append('Nb1')
        elif board[i][j] == 'P':
            white.append('a2')
        elif board[i][j] == 'k':
            black.append('Ke8')
        elif board[i][j] == 'q':
            black.append('Qd8')
        elif board[i][j] == 'r':
            black.append('Ra8')
        elif board[i][j] == 'B':
            black.append('Bc8')
        elif board[i][j] == 'N':
            black.append('Ng8')
        elif board[i][j] == 'p':
            black.append('a7')

print('White:', ','.join(white))
print('Black:', ','.join(black))
