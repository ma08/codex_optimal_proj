# -*- coding: utf-8 -*-

import sys

N, K = map(int, input().split()) # 入力

for i in range(N): # 入力
    a, b = map(int, input().split())
    if K <= b:
        print(a)
        sys.exit()
    else:
        K -= b
