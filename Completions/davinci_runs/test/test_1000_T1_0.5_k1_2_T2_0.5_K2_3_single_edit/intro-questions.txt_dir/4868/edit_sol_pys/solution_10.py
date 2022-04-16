
import sys

    print('+---+---+---+---+---+---+---+---+')
def main():
    for line in sys.stdin:
        line = line.strip()
        pieces = line.split(':')
        board = [['.' for i in range(8)] for j in range(8)]
        for i in range(1, len(pieces)):
            for piece in pieces[i].split(','):
                if piece == "":
                    continue
                board[ord(piece[2]) - ord('1')][ord(piece[1]) - ord('a')] = piece[0].lower()
                if piece[0].isupper():
                    board[ord(piece[2]) - ord('1')][ord(piece[1]) - ord('a')] = piece[0].upper()
        sys.stdout.write('|')
        for i in range(8):
            for j in range(8):
                print(board[i][j] + ':' if (i + j) % 2 == 0 else '.', end='')
            sys.stdout.write('|\n')
        sys.stdout.write('+---+---+---+---+---+---+---+---+\n')

if __name__ == '__main__':
    main()
