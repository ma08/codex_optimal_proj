

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().strip().split())
    print(n * a // (a + b))

if __name__ == '__main__':
    main()