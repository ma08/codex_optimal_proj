# -*- coding: utf-8 -*-

K = int(input())
S = input()

if K >= len(S):
    print(S)
else:
    print(S[:K] + '...')
