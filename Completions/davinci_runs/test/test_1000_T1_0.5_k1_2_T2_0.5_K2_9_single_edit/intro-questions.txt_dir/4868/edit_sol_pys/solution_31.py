
board = [['.'] * 8 for i in range(8)]

for i in range(2):
    color = input().split(':')[0].strip()
    pieces = input().split(':')[1].strip().split(',')
    for piece in pieces:
        if piece[0] == 'K':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'K'
        if piece[0] == 'Q':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'Q'
        if piece[0] == 'R':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'R'
        if piece[0] == 'B':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'B'
        if piece[0] == 'N':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'N'
        if piece[0] == 'P':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'P'
        if piece[0] == 'a':
            board[int(piece[1]) - 1][0] = 'P'
        if piece[0] == 'b':
            board[int(piece[1]) - 1][1] = 'P'
        if piece[0] == 'c':
            board[int(piece[1]) - 1][2] = 'P'
        if piece[0] == 'd':
            board[int(piece[1]) - 1][3] = 'P'
        if piece[0] == 'e':
            board[int(piece[1]) - 1][4] = 'P'
        if piece[0] == 'f':
            board[int(piece[1]) - 1][5] = 'P'
        if piece[0] == 'g':
            board[int(piece[1]) - 1][6] = 'P'
        if piece[0] == 'h':
            board[int(piece[1]) - 1][7] = 'P'

for i in range(8):
    for j in range(8):
        if board[i][j] == 'K':
            board[i][j] = 'k'
        if board[i][j] == 'Q':
            board[i][j] = 'q'
        if board[i][j] == 'R':
            board[i][j] = 'r'
        if board[i][j] == 'B':
            board[i][j] = 'b'
        if board[i][j] == 'N':
            board[i][j] = 'n'
        if board[i][j] == 'P':
            board[i][j] = 'p'

print('+---+---+---+---+---+---+---+---+')
for i in range(8):
    print('|' + ':'.join(board[i]) + '|')
    print('+---+---+---+---+---+---+---+---+')
