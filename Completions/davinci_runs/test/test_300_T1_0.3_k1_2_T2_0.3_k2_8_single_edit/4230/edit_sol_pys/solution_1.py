# -*- coding: utf-8 -*-

import sys

def main():
    x, n = map(int, sys.stdin.readline().split())
    p = list(map(int, sys.stdin.readline().split()))
    p.sort()
    ans = 0
    if x < p[0]:
        ans = p[0] - x
    elif x > p[-1]:
        ans = x - p[-1]
    else:
        for i in range(n-1):
            if p[i] < x and x < p[i+1]:
                if x - p[i] < p[i+1] - x:
                    ans = p[i+1] - x
                else:
                    ans = x - p[i]
    print(ans)

if __name__ == '__main__':
    main()
