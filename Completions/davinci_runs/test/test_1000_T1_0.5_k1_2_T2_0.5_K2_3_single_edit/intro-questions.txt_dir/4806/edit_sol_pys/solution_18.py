

import sys

line = sys.stdin.readline()

state = 0

for c in line:
    if c == 'R' or c == 'B' or c == 'L':
        if c == 'R':
            if state == 0:
                print('S', end='')
                state = 1
            else:
                print('H', end='')
                state = 0
        elif c == 'B':
            if state == 0:
                print('K', end='')
                state = 1
            else:
                print('H', end='')
                state = 0
        else:
            print('H', end='')
            state = 0
    else:
        print('Invalid move: ' + c)
        exit(0)
