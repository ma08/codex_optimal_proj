#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve(n, l):
    m = 0
    d = {}
    for i in l:
        if i in d:
            continue
        d[i] = 1
        for j in range(32):
            if i + 2**j in d:
                d[i + 2**j] = d[i] + 1
            if i - 2**j in d:
                d[i - 2**j] = d[i] + 1
            m = max(m, d[i])

    print(m)

    for i in l:
        if d[i] == m:
            print(i, end=' ')


if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))
    solve(n, l)
