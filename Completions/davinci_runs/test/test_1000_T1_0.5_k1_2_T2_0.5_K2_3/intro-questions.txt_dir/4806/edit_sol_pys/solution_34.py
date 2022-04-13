# https://atcoder.jp/contests/abc124/tasks/abc124_c

import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = input()
    result = []
    for i in range(len(moves)):
        if moves[i] == 'R':
            result.append('S')
        elif moves[i] == 'B':
            result.append('K')
        else:
            result.append('H')
    for i in range(len(moves)-2): # ループの最後にある2文字はチェックしない
        if moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'L':
            result[i] = 'C'
            result[i+1] = 'C'
            result[i+2] = 'C'
    print(''.join(result))

if __name__ == '__main__':
    main()
