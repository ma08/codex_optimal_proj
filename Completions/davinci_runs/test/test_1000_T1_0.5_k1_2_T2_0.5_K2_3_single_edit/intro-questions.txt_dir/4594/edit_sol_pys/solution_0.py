# coding: utf-8

import sys

N = int(sys.stdin.readline())
d_list = set()
for i in range(N):
    d_list.add(int(sys.stdin.readline()))
print(len(d_list))
