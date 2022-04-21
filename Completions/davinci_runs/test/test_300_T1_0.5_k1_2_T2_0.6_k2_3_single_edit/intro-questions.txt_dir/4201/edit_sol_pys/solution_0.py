#!/usr/bin/env python
# -*- coding: utf-8 -*-


def paint_red(h, w, k):
    ans = 0
    for i in range(2 ** h):
        t = bin(i)[2:].zfill(h)
        for j in range(2 ** w):
            s = bin(j)[2:].zfill(w)
            if t.count('1') + s.count('1') == k:
                ans += 1
    return ans

h, w, k = map(int, input().split())

print(paint_red(h, w, k))
