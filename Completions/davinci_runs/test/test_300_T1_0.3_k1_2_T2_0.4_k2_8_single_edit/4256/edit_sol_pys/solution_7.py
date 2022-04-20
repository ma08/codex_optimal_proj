

import sys

if __name__ == '__main__':
    A, B, C = map(int, sys.stdin.readline().split())
    print(min(B // A, C))
