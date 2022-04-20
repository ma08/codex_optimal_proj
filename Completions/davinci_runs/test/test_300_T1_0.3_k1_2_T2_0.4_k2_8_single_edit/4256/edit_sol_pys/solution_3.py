

import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    print(min(B // A, C)) if N < 1000 else print(0)
