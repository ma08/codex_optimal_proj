
#!/usr/bin/env python3

import sys

def Solve(a, b, c):
    if a + b == c:
        return '%d+%d=%d' % (a, b, c)
    if a - b == c:
        return '%d-%d=%d' % (a, b, c)
    if a * b == c:
        return '%d*%d=%d' % (a, b, c)
    if a == b * c and b != 0:
        return '%d=%d*%d' % (a, b, c)
    if a == b / c and b != 0:
        return '%d=%d/%d' % (a, b, c)
    if a / b == c and b != 0:
        return '%d/%d=%d' % (a, b, c)

def main():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print(Solve(a, b, c))

if __name__ == '__main__':
    main()
