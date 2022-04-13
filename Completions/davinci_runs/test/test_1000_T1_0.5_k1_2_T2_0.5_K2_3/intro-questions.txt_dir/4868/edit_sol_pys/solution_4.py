

def main():
    white_pieces = raw_input().split(': ')[1]
    black_pieces = raw_input().split(': ')[1]
    if white_pieces == '-':
        white_pieces = []
    else:
        white_pieces = white_pieces.split(',')
        white_pieces = [piece[0] + piece[1].lower() for piece in white_pieces]
    if black_pieces == '-':
        black_pieces = []
    else:
        black_pieces = black_pieces.split(',')
        black_pieces = [piece[0] + piece[1].lower() for piece in black_pieces]

    if not white_pieces and not black_pieces:
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
        print('|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|:::::::|')
    else:
        board = [list('........') for _ in range(8)]
        for piece in white_pieces:
            board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0].upper()
        for piece in black_pieces:
            board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0].lower()
        print('+---+---+---+---+---+---+---+---+')
        for row in board:
            print('|' + '|'.join(['.' + piece + '.' if piece != '.' else ':::' for piece in row]) + '|')
            print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
