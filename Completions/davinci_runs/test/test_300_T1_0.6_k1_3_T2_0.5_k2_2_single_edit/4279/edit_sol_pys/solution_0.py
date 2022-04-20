#!/usr/bin/env python3

import sys

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(solve(k))

def solve(k):
    n = 1
    while n*(n+1) < 2*k: # n(n+1)/2 < k
        n += 1
    if n*(n+1) == 2*k: # n(n+1)/2 = k
        return 0
    else:
        m = n*(n+1)//2 # n(n+1)/2
        return k-m

if __name__ == "__main__":
    main()
