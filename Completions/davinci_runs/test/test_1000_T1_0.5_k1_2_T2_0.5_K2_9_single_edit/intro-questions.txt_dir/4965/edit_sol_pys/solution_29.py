#!/usr/bin/env python3

import sys

def rearrange(n, t):
    t = sorted(t, reverse=True)
    if n%2 == 0:
        t1 = t[:n//2]
        t2 = t[n//2:]
    else:
        t1 = t[:n//2]
        t2 = t[n//2+1:]
    t1 = t1 + t2
    return t1

if __name__ == "__main__":
    n = int(input())
    t = [int(x) for x in input().split()]
    print(*rearrange(n, t))
