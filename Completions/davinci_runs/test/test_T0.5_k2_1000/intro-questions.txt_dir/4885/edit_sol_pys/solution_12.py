
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
            white.append('Kd8')
        elif board[i][j] == 'Q':
            white.append('Qe8')
        elif board[i][j] == 'R':
            white.append('Rh8')
        elif board[i][j] == 'B':
            white.append('Bf8')
        elif board[i][j] == 'N':
            white.append('Nb8')
        elif board[i][j] == 'P':
            white.append('a2')
        elif board[i][j] == 'k':
            black.append('Kd1')
        elif board[i][j] == 'q':
            black.append('Qe1')
        elif board[i][j] == 'r':
            black.append('Rh1')
        elif board[i][j] == 'b':
            black.append('Bf1')
        elif board[i][j] == 'n':
            black.append('Ng1')
        elif board[i][j] == 'p':
            black.append('a7')

print('White:', ','.join(white))
print('Black:', ','.join(black))
