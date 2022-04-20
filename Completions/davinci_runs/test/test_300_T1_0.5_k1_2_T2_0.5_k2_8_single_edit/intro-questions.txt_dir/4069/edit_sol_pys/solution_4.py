

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    if abs(x) < k * d:
        print(min(abs(x - (x // d) * d), abs(x - (x // d + 1) * d)))
    else:
        print(abs(x) - (k * d))

if __name__ == '__main__':
    main()
