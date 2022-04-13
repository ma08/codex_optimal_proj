
import sys
import math

def main():
    board = [['.'] * 8 for _ in range(8)]
    for i in range(2):
        line = sys.stdin.readline().split(':')
        for j in range(1, len(line)):
            piece = line[j].split(',')
            for k in range(len(piece)):
                if piece[k] == '':
                    continue
                if piece[k][0] != ' ':
                    piece[k] = ' ' + piece[k]
                row = int(piece[k][2]) - 1
                if piece[k][3].isalpha():
                    col = ord(piece[k][3]) - ord('a')
                else:
                    col = int(piece[k][3]) - 1
                board[row][col] = piece[k][1].lower() if i == 1 else piece[k][1]
    for i in range(8):
        print('+---+---+---+---+---+---+---+---+')
        print('|' + '|'.join(board[i]) + '|')
    print('+---+---+---+---+---+---+---+---+')

if __name__ == '__main__':
    main()
