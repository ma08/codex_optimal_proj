

import sys

def main():
    board = [['.' for i in range(8)] for j in range(8)]
    board[7][0] = board[7][7] = 'r'
    board[0][0] = board[0][7] = 'R'
    board[7][1] = board[7][6] = 'n'
    board[0][1] = board[0][6] = 'N'
    board[7][2] = board[7][5] = 'b'
    board[0][2] = board[0][5] = 'B'
    board[7][3] = 'q'
    board[0][3] = 'Q'
    board[7][4] = 'k'
    board[0][4] = 'K'
    for i in range(8):
        board[1][i] = 'p'
        board[6][i] = 'P'
    
    for line in sys.stdin:
        for piece in line.split(',')[1:]:
            color = piece[0]
            piece = piece[1:]
            piece_type = piece[0]
            row = int(piece[1]) - 1
            column = ord(piece[2]) - ord('a')
            if piece_type == 'K':
                board[row][column] = 'K' if color == 'W' else 'k'
            elif piece_type == 'Q':
                board[row][column] = 'Q' if color == 'W' else 'q'
            elif piece_type == 'R':
                board[row][column] = 'R' if color == 'W' else 'r'
            elif piece_type == 'B':
                board[row][column] = 'B' if color == 'W' else 'b'
            elif piece_type == 'N':
                board[row][column] = 'N' if color == 'W' else 'n'
            elif piece_type == 'P':
                board[row][column] = 'P' if color == 'W' else 'p'
            elif piece_type == 'a':
                board[row][0] = 'P' if color == 'W' else 'p'
            elif piece_type == 'h':
                board[row][7] = 'P' if color == 'W' else 'p'
    
    print('+---+---+---+---+---+---+---+---+')
    for row in board:
        print('|' + '|'.join([':' + p.lower() + ':' if p.isupper() else '.' + p + '.' for p in row]) + '|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()