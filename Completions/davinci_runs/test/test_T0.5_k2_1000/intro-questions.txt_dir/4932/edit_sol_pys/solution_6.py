

import sys

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())

    for i in [p, m, g]:
        if i > a and (i - a) % (b + a) < a:
            print('both')
        elif i > a:
            print('one')
        elif i <= a:
            print('both')

        if i > c and (i - c) % (c + d) < c:
            print('one')
        elif i > c:
            print('none')
        elif i <= c:
            print('both')


if __name__ == '__main__':
    main()
