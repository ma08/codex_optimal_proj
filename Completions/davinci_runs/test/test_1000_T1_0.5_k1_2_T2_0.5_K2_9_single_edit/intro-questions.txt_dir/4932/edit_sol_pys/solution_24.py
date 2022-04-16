

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    if p > a:
        if (p - a) % (b + a) < a:
            print('both')
        else: 
            print('one')
    else:
        print('both')

    if m > a:
        if (m - a) % (b + a) < a:
            print('both')
        else: 
            print('one')
    else:
        print('both')

    if g > a:
        if (g - a) % (b + a) < a:
            print('both')
        else: 
            print('one')
    else:
        print('both')

    if p > c:
        if (p - c) % (c + d) < c:
            print('both')
        else: 
            print('one')
    else:
        print('both')

    if m > c:
        if (m - c) % (c + d) < c:
            print('both')
        else: 
            print('one')
    else:
        print('both')

    if g > c:
        if (g - c) % (c + d) < c:
            print('both')
        else: 
            print('one')
    else:
        print('both')


if __name__ == '__main__':
    main()
