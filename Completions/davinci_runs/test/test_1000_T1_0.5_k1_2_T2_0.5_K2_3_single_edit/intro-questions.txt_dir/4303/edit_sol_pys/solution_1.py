# coding: utf-8

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    x = list(map(int, sys.stdin.readline().split()))
    # print(N, K, x)
    x.sort()
    # print(x)
    # print(x[K-1] - x[0])
    print(min(abs(x[K-1] - x[0]), abs(x[-1] - x[K-1])) + x[K-1] - x[0])

if __name__ == "__main__":
    main()
