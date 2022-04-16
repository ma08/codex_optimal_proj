
import sys

def main():
    board = []
    for line in sys.stdin:
        board.append(line.strip())

    white = ""
    black = ""

    for i in range(len(board)):
        for j in range(len(board[0])):
            pos = board[i][j]
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
