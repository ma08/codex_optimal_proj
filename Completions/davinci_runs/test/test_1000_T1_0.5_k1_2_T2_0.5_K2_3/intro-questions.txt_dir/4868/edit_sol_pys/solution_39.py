

board = [['.'] * 8 for i in range(8)]

for i in range(2):
    color = input().split(':')[0].strip().lower()
    pieces = input().split(':')[1].strip().lower().split(',')
    for piece in pieces:
        if piece[0] == 'K':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'k'
        elif piece[0] == 'Q':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'q'
        elif piece[0] == 'R':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'r'
        elif piece[0] == 'B':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'b'
        elif piece[0] == 'N':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'n'
        elif piece[0] == 'P':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'p'
        elif piece[0] == 'a':
            board[int(piece[1]) - 1][0] = 'p'
        elif piece[0] == 'b':
            board[int(piece[1]) - 1][1] = 'p'
        elif piece[0] == 'c':
            board[int(piece[1]) - 1][2] = 'p'
        elif piece[0] == 'd':
            board[int(piece[1]) - 1][3] = 'p'
        elif piece[0] == 'e':
            board[int(piece[1]) - 1][4] = 'p'
        elif piece[0] == 'f':
            board[int(piece[1]) - 1][5] = 'p'
        elif piece[0] == 'g':
            board[int(piece[1]) - 1][6] = 'p'
        elif piece[0] == 'h':
            board[int(piece[1]) - 1][7] = 'p'

for i in range(8):
    for j in range(8):
        if board[i][j] == 'K':
            board[i][j] = 'k'
        elif board[i][j] == 'Q':
            board[i][j] = 'q'
        elif board[i][j] == 'R':
            board[i][j] = 'r'
        elif board[i][j] == 'B':
            board[i][j] = 'b'
        elif board[i][j] == 'N':
            board[i][j] = 'n'
        elif board[i][j] == 'P':
            board[i][j] = 'p'

print('+---+---+---+---+---+---+---+---+')
for i in range(8):
    print('| ' + ':'.join(board[i]) + ' |')
    print('+---+---+---+---+---+---+---+---+')
