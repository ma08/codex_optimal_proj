#!/usr/bin/env python3

import sys

def main():
    N, K = map(int, sys.stdin.readline().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - N % K))

if __name__ == '__main__':
    main()
