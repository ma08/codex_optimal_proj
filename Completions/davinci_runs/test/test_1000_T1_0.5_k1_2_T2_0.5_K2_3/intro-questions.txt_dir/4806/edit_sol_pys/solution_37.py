# https://atcoder.jp/contests/abc124/tasks/abc124_c

import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = list(input())
    result = []
    for i in range(len(moves)):
        if moves[i] == 'R' and i % 2 == 0:
            result.append('S')
        elif moves[i] == 'B' and i % 2 == 0:
            result.append('K')
        elif moves[i] == 'R' and i % 2 == 1:
            result.append('K')
        elif moves[i] == 'B' and i % 2 == 1:
            result.append('H')
    print(''.join(result))

if __name__ == '__main__':
    main()
