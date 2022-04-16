

import sys

def main():
    carrots = 1
    n, p = map(int, sys.stdin.readline().split())
    for i in range(n):
        sys.stdin.readline()
        carrots += p
    print carrots

if __name__ == '__main__':
    main()
