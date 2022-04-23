# -*- coding: utf-8 -*-

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    if s % n != 0:
        print(-1)
        return
    ans = 0; cnt = 0; s //= n
    for i in range(n):
        if a[i] != s:
            cnt += 1
        else:
            ans += cnt
            cnt = 0
    print(ans)

if __name__ == '__main__':
    main()
