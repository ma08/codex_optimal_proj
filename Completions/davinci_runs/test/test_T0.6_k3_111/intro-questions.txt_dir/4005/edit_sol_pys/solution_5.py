#!/usr/bin/python

import sys

def main():
    (x1, y1, x2, y2) = map(int, sys.stdin.readline().split())
    (x3, y3, x4, y4) = map(int, sys.stdin.readline().split())
    (x5, y5, x6, y6) = map(int, sys.stdin.readline().split())
    if (x1 < x4 and x2 > x3) and (y1 < y4 and y2 > y3):
        print('YES')
    elif (x1 < x6 and x2 > x5) and (y1 < y6 and y2 > y5):
        print('YES')
    else:
        print('NO')

main()
