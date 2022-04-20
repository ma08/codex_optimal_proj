# -*- coding: utf-8 -*-

import math

def main():
    n, m = map(int, input().split())
    a = [int(x) for x in input().split()]
    a.sort()

    ans = 0
    for i in range(m):
        if a[i] < 0:
            ans += -a[i]
    print(ans)

if __name__ == '__main__':
    main()
