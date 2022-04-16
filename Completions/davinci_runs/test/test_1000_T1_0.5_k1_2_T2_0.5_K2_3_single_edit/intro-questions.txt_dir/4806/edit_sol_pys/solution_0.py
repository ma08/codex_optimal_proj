import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = input()
    result = deque()
    for i in range(len(moves)):
        if moves[i] == 'R':
            result.append('S') # スマホ
        elif moves[i] == 'B':
            result.append('K') # キーボード
        else:
            result.append('H') # マウス
    for i in range(len(moves)-2):
        if moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'L':
            result[i] = 'C' # スマホ
            result[i+1] = 'C' # キーボード
            result[i+2] = 'C' # マウス
    print(''.join(result))

if __name__ == '__main__':
    main()
