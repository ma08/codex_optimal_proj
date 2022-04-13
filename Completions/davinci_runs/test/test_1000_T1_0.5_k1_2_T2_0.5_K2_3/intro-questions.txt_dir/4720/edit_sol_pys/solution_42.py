#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 :

N = int(input())
S = [0] * 100001
for i in range(N):
    l, r = map(int, input().split())
    for j in range(l, r + 1):
        S[j] = 1
print(sum(S))
