


def get_piece(piece):
    piece_dict = {
        'K': 'K',
        'Q': 'Q',
        'R': 'R',
        'B': 'B',
        'N': 'N',
        'P': 'P',
        'a': 'P',
        'b': 'P',
        'c': 'P',
        'd': 'P',
        'e': 'P',
        'f': 'P',
        'g': 'P',
        'h': 'P'
    }
    return piece_dict[piece]
board = [['.'] * 8 for i in range(8)]

for i in range(2):
    color = input().split(':')[0].strip()
    pieces = input().split(':')[1].strip().split(',')
    for piece in pieces:
        if len(piece) == 3:
            board[int(piece[2]) - 1][ord(piece[1]) - ord('a')] = get_piece(piece[0])
        else:
            board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = get_piece(piece[0])

for i in range(8):
    for j in range(8):
        if board[i][j] != '.' and board[i][j].isupper():
            board[i][j] = board[i][j].lower()

print('+---+---+---+---+---+---+---+---+')
for i in range(8):
    print('|' + ':'.join(board[i]) + '|')
    print('+---+---+---+---+---+---+---+---+')
