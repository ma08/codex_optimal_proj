# coding: utf-8

import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(k - 1):
    print(x - k + 1 + i, end=" ")  # end=" " で改行しない

print(x - 1)  # 最後は改行する
