#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for i in range(n)]
    a.sort()
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur * a[i])
    print(ans)

if __name__ == '__main__':
    main()
