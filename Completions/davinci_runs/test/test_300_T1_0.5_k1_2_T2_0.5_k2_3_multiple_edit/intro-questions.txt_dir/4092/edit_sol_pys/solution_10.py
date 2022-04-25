# -*- coding: utf-8 -*-

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    ans = 0
    for i in range(k):
        ans += a[i]
    print(ans)    

if __name__ == '__main__':
    main()
