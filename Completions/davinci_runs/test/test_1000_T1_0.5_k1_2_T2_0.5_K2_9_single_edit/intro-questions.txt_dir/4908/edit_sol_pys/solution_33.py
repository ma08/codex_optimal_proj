
import sys


def solve(a, b, c):
    if a + b == c:
        return '%d+%d=%d' % (a, b, c)
    if a - b == c:
        return '%d-%d=%d' % (a, b, c)
    if a * b == c:
        return '%d*%d=%d' % (a, b, c)
    if a == b * c:
        return '%d=%d*%d' % (a, b, c)
    if a == b / c:
        return '%d=%d/%d' % (a, b, c)
    if a / b == c:
        return '%d/%d=%d' % (a, b, c)


def main():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print(solve(a, b, c))

if __name__ == '__main__':
    main()
