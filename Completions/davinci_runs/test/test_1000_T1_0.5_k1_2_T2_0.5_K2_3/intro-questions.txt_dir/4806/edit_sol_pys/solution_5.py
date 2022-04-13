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
    print(''.join(result))

if __name__ == '__main__':
    main()
