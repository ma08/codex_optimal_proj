#!/usr/bin/env python3
import sys

def main():
    board = []
    for line in sys.stdin:
        board.append(line.strip())

    white = ""
    black = ""

    for i, row in enumerate(board): # for each row
        for j, pos in enumerate(row): # for each position in that row
            if pos == '.':
                continue
            if pos.isupper(): # white piece
                white += pos.lower() + chr(j + ord('a')) + str(8 - i) + ','
            else: # black piece
                black += pos.upper() + chr(j + ord('a')) + str(8 - i) + ','

    print('White: ' + white[:-1]) # remove trailing comma
    print('Black: ' + black[:-1]) # remove trailing comma

if __name__ == '__main__':
    main()
