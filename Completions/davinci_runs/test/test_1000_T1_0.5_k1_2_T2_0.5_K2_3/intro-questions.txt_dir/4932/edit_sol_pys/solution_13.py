
import os
import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    for i in [p, m, g]:
        if i > a and (i - a) % (b + a) < a:
            print('one')
        else:
            print('both')

        if i > c and (i - c) % (c + d) < c:
            print('one')
        else:
            print('both')


if __name__ == '__main__':
    main()
