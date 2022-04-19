# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_dif = sys.maxsize
    min_idx = 0
    for i in range(n):
        dif = abs(t - h[i] * 0.006 - a)
        if dif < min_dif:
            min_dif = dif
            min_idx = i
    print(min_idx + 1)

if __name__ == '__main__':
    main()
