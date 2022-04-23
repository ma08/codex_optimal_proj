# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        ans += abs(a[i] - (i+1))
    print(ans)

if __name__ == '__main__':
    main()
