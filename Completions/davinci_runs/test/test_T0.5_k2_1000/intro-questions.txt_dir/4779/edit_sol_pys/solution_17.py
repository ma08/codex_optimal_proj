#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(sys.stdin.readline()) for i in range(n)]
    a.sort()
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur * a[i])
    print(ans)

if __name__ == '__main__':
    main()
