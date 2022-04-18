

import sys

def Solve(a, b, c):
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
    return 'No solution'
def main():
    a, b, c = map(int, sys.stdin.readline().strip().split())
    print(Solve(a, b, c))

if __name__ == '__main__':
    main()
