

import sys

def main(pname):
    sys.stdin = open(pname + '.in', 'r') # open input file
    sys.stdout = open(pname + '.out', 'w') # open output file

    x, y = [int(i) for i in input().split()] # read input

    if y == 1:
        print('IMPOSSIBLE')
        return
    if x == 0:
        print('ALL GOOD')
        return

    print(int(-x / (y - 1)))

if __name__ == "__main__":
    main('file')
