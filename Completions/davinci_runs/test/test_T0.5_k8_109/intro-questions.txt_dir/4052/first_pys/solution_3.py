

import sys

def main():
    # read input
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    # init
    moves = []
    for i in range(n):
        if s[i] != t[i]:
            moves.append(i)

    # check if possible
    if len(moves) > 10000:
        print('-1')
        return

    # print moves
    print(len(moves))
    for i in moves:
        print(i + 1, end=' ')
    print()

if __name__ == '__main__':
    main()