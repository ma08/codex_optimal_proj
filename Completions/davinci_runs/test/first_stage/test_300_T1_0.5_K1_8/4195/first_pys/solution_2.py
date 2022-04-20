

import sys

def main():
    d, n = [int(x) for x in sys.stdin.readline().split()]
    if d == 0:
        print(n)
    elif d == 1:
        print(100 * n)
    elif d == 2:
        print(10000 * n)

if __name__ == '__main__':
    main()