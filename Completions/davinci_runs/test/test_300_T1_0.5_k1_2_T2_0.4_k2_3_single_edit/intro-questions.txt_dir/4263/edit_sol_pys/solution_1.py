#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main():
    N = int(sys.stdin.readline().rstrip())
    A = [int(i) for i in sys.stdin.readline().rstrip().split()]
    A.sort()
    for i in range(N):
        if i == N - 1:
            print(A[i])
        else:
            print(A[i], end=' ')

if __name__ == '__main__':
    main()
