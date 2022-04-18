

def main():
    white_pieces = [piece[0] + piece[1].lower() for piece in input().split(': ')[1].split(', ')]
    black_pieces = [piece[0] + piece[1].lower() for piece in input().split(': ')[1].split(', ')]
    board = [list('........') for _ in range(8)]
    for piece in white_pieces:
        board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0].upper()
    for piece in black_pieces:
        board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0].lower()
    print('+---+---+---+---+---+---+---+---+')
    for row in board:
        print('|' + '|'.join(['.' + piece.upper() + '.' if piece != '.' else ':::' for piece in row]) + '|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
