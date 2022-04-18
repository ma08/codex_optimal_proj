import sys

board = []

for line in sys.stdin:
    board.append(line[:-1])

white = []
black = []

for i in range(8):
    for j in range(8):
        if board[i][j] == '.':
            continue
        piece = board[i][j]
        if piece.isupper():
            white.append(piece + chr(97 + j) + str(8 - i))
        else:
            black.append(piece.upper() + chr(97 + j) + str(8 - i))

print("White: " + ", ".join(white))
print("Black: " + ", ".join(black))
