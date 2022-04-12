#!/usr/bin/env python3

import sys

def main():
    n = int(sys.stdin.readline()) # get n
    a = []
    for i in range(n):
        a.append(int(sys.stdin.readline())) # get a[i]
    a.sort() # sort a
    ans = 0
    cur = 0
    for i in range(n):
        cur += a[i]
        ans = max(ans, cur * a[i]) # update ans
    print(ans)

if __name__ == '__main__':
    main()
