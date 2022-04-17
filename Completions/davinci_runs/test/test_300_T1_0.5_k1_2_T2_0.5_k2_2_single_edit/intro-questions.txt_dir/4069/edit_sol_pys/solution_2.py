

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if abs(a) < b * c:
        print(abs(a - (a // c) * c))
    else:
        print(abs(a) - (b * c))

if __name__ == '__main__':
    main()
