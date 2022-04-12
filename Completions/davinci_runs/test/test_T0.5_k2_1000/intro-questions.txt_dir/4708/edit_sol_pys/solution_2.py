#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    import sys

    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    X = int(sys.stdin.readline())
    Y = int(sys.stdin.readline())

    if N <= K:
        print(N * X)
    elif N > K:
        print(K * X + (N - K) * Y)

if __name__ == '__main__':
    main()
