

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    x, y = [int(i) for i in input().split()]

    if y == 1:
        print('IMPOSSIBLE')
        return
    if x == 0:
        print('ALL GOOD')
        return

    print(-(x / (y - 1)))

if __name__ == "__main__":
    main('temperature')
