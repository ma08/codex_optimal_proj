

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    p, m, g = map(int, sys.stdin.readline().split())

    for i in [p, m, g]:
        if i > a or i > c:
            if (i - a) % (b + a) < a or (i - c) % (c + d) < c:
                print('both', end=' ')
            else:
                print('one', end=' ')
        else:
            print('both', end=' ')


if __name__ == '__main__':
    main()
