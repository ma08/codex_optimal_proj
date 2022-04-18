

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    x.sort()
    print(min(abs(x[K-1] - x[0]), abs(x[-1] - x[K-1])) + x[-1] - x[0])

if __name__ == "__main__":
    main()
