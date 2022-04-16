import os

import sys


def main():
    if len(sys.argv) < 2:
        print('Usage: python file.py <file>')
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print('File not found: ' + path)
        sys.exit(1)

    with open(path) as f:
        board = f.readlines()

    white = ""
    black = ""

    for i, row in enumerate(board):
        for j, pos in enumerate(row):
            if pos == '.':
                continue
            if pos.isupper():
                white += pos.lower() + chr(j + ord('a')) + str(8 - i) + ','
            else:
                black += pos.upper() + chr(j + ord('a')) + str(8 - i) + ','

    print('White: ' + white[:-1])
    print('Black: ' + black[:-1])

if __name__ == '__main__':
    main()
