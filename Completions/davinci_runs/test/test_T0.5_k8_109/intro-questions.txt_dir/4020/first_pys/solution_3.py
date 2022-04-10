

import sys

def main():
    h1, m1 = [int(x) for x in sys.stdin.readline().split(':')]
    h2, m2 = [int(x) for x in sys.stdin.readline().split(':')]

    m = (m1 + m2) / 2
    h = (h1 + h2) / 2
    if m == 60:
        h += 1
        m = 0

    print '%02d:%02d' % (h, m)

if __name__ == '__main__':
    main()