

import sys

def main():
    board = [['.' for i in range(8)] for j in range(8)]
    board[7][0] = board[7][7] = 'R'
    board[0][0] = board[0][7] = 'r'
    board[7][1] = board[7][6] = 'N'
    board[0][1] = board[0][6] = 'n'
    board[7][2] = board[7][5] = 'B'
    board[0][2] = board[0][5] = 'b'
    board[7][3] = 'q'
    board[0][3] = 'Q'
    board[7][4] = 'K'
    board[0][4] = 'k'
    for i in range(8):
        board[1][i] = 'P'
        board[6][i] = 'p'
    
    for line in sys.stdin.readlines():
        for piece in line.split(',')[1:]:
            color = piece[0]
            piece = piece[1:]
            piece_type = piece[0]
            row = int(piece[1]) - 1
            column = ord(piece[2]) - ord('a')
            if piece_type == 'P':
                board[row][column] = 'p' if color == 'W' else 'P'
            else:
                board[row][column] = piece_type.lower() if color == 'W' else piece_type.upper()
    
    print('+---+---+---+---+---+---+---+---+')
    for row in board:
        print('|' + '|'.join([':' + p.lower() + ':' if p.isupper() else '.' + p + '.' for p in row]) + '|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
