

import sys

def get_pos(piece):
    """
    Returns the row and column of a chess piece
    """
    return piece[2:3], piece[3:4]

def get_piece(piece):
    """
    Returns the chess piece type
    """
    return piece[0:1]

def get_color(piece):
    """
    Returns the color of the chess piece
    """
    return piece[1:2]

def get_index(row, col):
    """
    Returns the index of a position
    """
    return (int(row) - 1) * 8 + (ord(col) - ord('a'))

def get_pos_from_index(index):
    """
    Returns the position of a chess piece
    """
    return str((index / 8) + 1), chr(index % 8 + ord('a'))

def main():
    """
    Main function
    """
    white = sys.stdin.readline().split(',')
    black = sys.stdin.readline().split(',')
    board = ['' for _ in range(64)]

    for piece in white + black:
        row, col = get_pos(piece)
        index = get_index(row, col)
        board[index] = get_piece(piece).lower() if get_color(piece) == 'b' else get_piece(piece)

    print('+---+---+---+---+---+---+---+---+')
    for i in range(8):
        print('|' + '|'.join(board[i*8:(i+1)*8]) + '|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
