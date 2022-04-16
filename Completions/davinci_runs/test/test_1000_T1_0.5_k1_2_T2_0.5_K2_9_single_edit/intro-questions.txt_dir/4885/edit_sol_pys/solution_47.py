

import sys

def main():
    board = []
    for line in sys.stdin:
        board.append(line.strip())

    white = ""
    black = ""

    for i, row in enumerate(board, start=1):
        for j, pos in enumerate(row, start=1):
            if pos == '.':
                continue
            if pos.isupper():
                white += pos.lower() + chr(j + ord('a') - 1) + str(8 - i) + ','
            else:
                black += pos.upper() + chr(j + ord('a') - 1) + str(8 - i) + ','
    print(white)
    print(black)
    print('White: ' + white[:-1])
    print('Black: ' + black[:-1])

if __name__ == '__main__':
    main()
