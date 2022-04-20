

import sys

def main():
    a, b, c, k = map(int, sys.stdin.readline().split())
    print(a - min(k-a-b, 0))

if __name__ == '__main__':
    main()