#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abc096/tasks/abc096_b

def main():
    a, b, c = map(int, input().split())
    k = int(input())
    ans = a + b + c
    for i in range(k):
        if a < b:
            a *= 2
        elif b < c:
            b *= 2
        else:
            c *= 2
    print(ans - max(a, b, c))


if __name__ == '__main__':
    main()
