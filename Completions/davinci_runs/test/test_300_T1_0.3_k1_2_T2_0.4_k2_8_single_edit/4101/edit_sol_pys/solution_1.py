#!/usr/bin/env python3

import sys
import math

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = []
    for i in range(n):
        a.append(list(map(int, sys.stdin.readline().split())))
    r = [0] * n
    c = [0] * m
    for i in range(n):
        for j in range(m):
            if a[i][j] == i % 2:
                r[i] = 1
            if a[i][j] == j % 2:
                c[j] = 1
    for i in range(n):
        for j in range(m):
            if (a[i][j] == 0 and r[i] + c[j] == 1) or (a[i][j] == 1 and r[i] + c[j] == 0):
                print("NO")
                return
    print("YES")
    print("".join(map(str, r)))
    print("".join(map(str, c)))

if __name__ == "__main__":
    main()
