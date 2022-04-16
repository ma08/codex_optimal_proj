

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        pieces = line.split(":")
        board = [['.' for i in range(8)] for j in range(8)]
        for piece in pieces[1].split(","):
            if piece == "":
                continue
            board[ord(piece[2]) - ord('1')][ord(piece[1]) - ord('a')] = piece[0].lower()
            if piece[0].isupper():
                board[ord(piece[2]) - ord('1')][ord(piece[1]) - ord('a')] = piece[0].upper()
        print('+---+---+---+---+---+---+---+---+')
        for i in range(8):
            print('|', end='')
            for j in range(8):
                print(board[i][j] + ':' if (i + j) % 2 == 0 else '.', end='')
            print('|')
        print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
