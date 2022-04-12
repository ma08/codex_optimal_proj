#!/usr/bin/env python3

import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]  # h: height, n: number of horizontal cuts, m: number of vertical cuts
    a = b = 0
    for i in range(1,h+1):
        a += 2*i
        b += i
    if a <= n:
        a = 0
    else:
        a -= n
    if b <= m:
        b = 0
    else:
        b -= m
    print(a, b)

if __name__ == '__main__':
    main()
