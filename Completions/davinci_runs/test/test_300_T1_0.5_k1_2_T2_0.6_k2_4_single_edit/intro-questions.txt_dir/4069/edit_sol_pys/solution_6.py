

import sys

def main():
    x, k, d = map(int, sys.stdin.readline().rstrip().split())
    x = abs(x)
    print(min(x, (x - d*k) % (2*d)))

if __name__ == '__main__':
    main()
