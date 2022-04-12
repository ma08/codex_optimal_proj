

def main():
    white_pieces = input().split(': ')[1].split(', ') # split on ': ' and then on ', '
    white_pieces = [piece[0].lower() + piece[1].lower() for piece in white_pieces] # convert to lowercase
    black_pieces = input().split(': ')[1].split(', ') # split on ': ' and then on ', '
    black_pieces = [piece[0].lower() + piece[1].lower() for piece in black_pieces] # convert to lowercase
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
