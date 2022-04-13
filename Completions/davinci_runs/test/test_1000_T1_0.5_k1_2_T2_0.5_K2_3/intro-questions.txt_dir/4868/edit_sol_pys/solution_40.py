

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        pieces = line.split(":") if line.find(":") != -1 else [line]
        board = [['.' for i in range(8)] for j in range(8)]
        for i in range(1, len(pieces)):
            for piece in pieces[i].split(","):
                if piece == "":
                    continue
                board[7 - (ord(piece[2]) - ord('1'))][ord(piece[1]) - ord('a')] = piece[0].lower()
                if piece[0].isupper():
                    board[7 - (ord(piece[2]) - ord('1'))][ord(piece[1]) - ord('a')] = piece[0].upper()
        print('+---+---+---+---+---+---+---+---+')
        for i in range(8):
            print('|', end='')
            for j in range(8):
                print(board[i][j] + ':' if (i + j) % 2 == 0 else '.', end='')
            print('|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
