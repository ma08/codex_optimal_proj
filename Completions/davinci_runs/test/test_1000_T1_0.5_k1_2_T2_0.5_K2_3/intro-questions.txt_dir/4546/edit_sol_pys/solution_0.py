
import sys

if __name__ == '__main__':
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if b - a == c - b:
        print('YES')
    else:
        print('NO')
