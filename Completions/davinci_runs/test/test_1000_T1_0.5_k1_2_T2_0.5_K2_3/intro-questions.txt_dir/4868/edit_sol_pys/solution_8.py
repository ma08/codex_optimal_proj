
def main(white_pieces, black_pieces):
    board = [['.' for _ in range(8)] for _ in range(8)]
    for w in white_pieces:
        board[ord(w[1]) - ord('1')][ord(w[0]) - ord('a')] = w[0].upper()
    for b in black_pieces:
        board[ord(b[1]) - ord('1')][ord(b[0]) - ord('a')] = b[0].lower()
        print('+---+---+---+---+---+---+---+---+')
    for row in board:
        print('|' + '|'.join(['.' + piece + '.' if piece != '.' else ':::' for piece in row]) + '|')
        print('+---+---+---+---+---+---+---+---+')
