

board = [['.'] * 8 for i in range(8)]

for i in range(2): 
    color = input().split(':')[0].strip()
    pieces = input().split(':')[1].strip().split(',')
    for piece in pieces:
        if piece[0] == 'K':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'K'
        elif piece[0] == 'Q':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'Q'
        elif piece[0] == 'R':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'R'
        elif piece[0] == 'B':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'B'
        elif piece[0] == 'N':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'N'
        elif piece[0] == 'P':
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = 'P'
        elif piece[0] == 'a' or piece[0] == 'b' or piece[0] == 'c' or piece[0] == 'd' or piece[0] == 'e' or piece[0] == 'f' or piece[0] == 'g' or piece[0] == 'h':
            board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = 'P'

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
