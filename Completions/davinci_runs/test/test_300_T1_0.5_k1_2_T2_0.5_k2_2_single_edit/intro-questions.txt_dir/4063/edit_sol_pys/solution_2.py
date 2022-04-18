#!/usr/bin/env python
# coding: utf-8
#
# Author:   Kazuto Nakashima
# URL:      http://kazuto1011.github.io
# Created:  2017-11-09
#
# Modified by:
#

n = int(input())
d = list(map(int, input().split()))

d.sort(reverse=True)

cnt = 0
for i in range(n//2):
    if d[i] == d[i+n//2]:
        cnt += 1
    else:
        break
print(n//2 + cnt)
