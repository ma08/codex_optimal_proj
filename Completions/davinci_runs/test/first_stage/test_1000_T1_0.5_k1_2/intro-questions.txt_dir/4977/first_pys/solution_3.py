

import sys

def main():
    a, b = map(int, sys.stdin.readline().strip().split())
    c, d = map(int, sys.stdin.readline().strip().split())
    t = int(sys.stdin.readline().strip())

    if abs(a - c) + abs(b - d) <= t and (abs(a - c) + abs(b - d)) % 2 == t % 2:
        print('Y')
    else:
        print('N')

if __name__ == '__main__':
    main()