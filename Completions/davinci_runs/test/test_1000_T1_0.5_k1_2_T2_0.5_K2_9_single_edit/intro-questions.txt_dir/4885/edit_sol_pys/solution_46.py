
import sys

def main():
    board = []
    for line in sys.stdin.readlines():
        board.append(line.strip())

    white = ""
    black = ""

    for i, row in enumerate(board):
        for j, pos in enumerate(row):
            if pos == '.':
                continue
            if pos.isupper(): # white
                white += pos.lower() + chr(j + ord('a')) + str(8 - i) + ','
            else: # black
                black += pos.upper() + chr(j + ord('a')) + str(8 - i) + ','

    print('White: ' + white[:-1] + '\n')
    print('Black: ' + black[:-1] + '\n')

if __name__ == '__main__':
    main()
