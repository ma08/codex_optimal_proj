#!/usr/bin/python

import sys

def solve(a):
    odd = 0
    for i in a:
        if i % 2 == 1:
            odd += 1

    if odd % 2 == 0:
        return 0
    else:
        return -1

if __name__ == '__main__':

    t = int(sys.stdin.readline())

    for i in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().strip().split()))

        print solve(a)
