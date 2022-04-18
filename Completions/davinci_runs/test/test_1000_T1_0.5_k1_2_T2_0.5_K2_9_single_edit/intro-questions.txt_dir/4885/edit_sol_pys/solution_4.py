

import sys

# 체스판 입력
sys.stdin = open('input.txt', 'r')

board = []
for i in range(8):
    board.append(list(input()))
# 백, 흑 말 위치 저장할 리스트


white = []
black = []
# 말 위치 저장


for i in range(8):
    for j in range(8):
        if board[i][j] == '.':
            continue
        elif ord(board[i][j]) < 97:
            white.append(board[i][j] + chr(ord('a') + j) + str(i + 1))
        else:
            black.append(board[i][j] + chr(ord('a') + j) + str(i + 1))

print('White:', ','.join(white))
print('Black:', ','.join(black))
