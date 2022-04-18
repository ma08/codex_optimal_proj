#!/usr/bin/env python

import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(sys.stdin.readline().strip()) for i in range(n)]
    a.sort()
    ans = 0
    cur = 0.0
    for e in a:
        cur += e
        ans = max(ans, cur * e)
    print(ans)

if __name__ == '__main__':
    main()
