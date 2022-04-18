

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    for i in [p, m, g]:
        a_mod = (i - a) % (b + a)
        c_mod = (i - c) % (c + d)
        if i > a and a_mod < a:
            print('one')
        else:
            print('both')

        if i > c and c_mod < c:
            print('one')
        else:
            print('both')


if __name__ == '__main__':
    main()
