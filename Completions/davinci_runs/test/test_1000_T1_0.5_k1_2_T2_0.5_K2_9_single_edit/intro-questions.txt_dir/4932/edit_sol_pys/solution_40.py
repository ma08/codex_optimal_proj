

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    for j in [p, m, g]:
        if j > a:
            if (j - a) % (b + a) < a:
                print('both')
            else:
                print('one')
        else:
            print('both')

        if j > c:
            if (j - c) % (c + d) < c:
                print('one')
            else:
                print('both')
        else:
            print('both')


if __name__ == '__main__':
    main()
