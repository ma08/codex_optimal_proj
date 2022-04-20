#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    n = int(input())
    A = list(map(int, input().split()))[:n]

    A.sort()
    print(A[-1] - A[0])

if __name__ == '__main__':
    main()
