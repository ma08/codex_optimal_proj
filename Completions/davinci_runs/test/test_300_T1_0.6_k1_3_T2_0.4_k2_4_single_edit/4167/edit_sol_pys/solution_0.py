#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys, re


def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    ans = 0 
    for i in range(1, N+1):
        if A <= sum(map(int, list(str(i)))) <= B:
            ans += i
    print(ans) 


if __name__ == '__main__':
    main()
