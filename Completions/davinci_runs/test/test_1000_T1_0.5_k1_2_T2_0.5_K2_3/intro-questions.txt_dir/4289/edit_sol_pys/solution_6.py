# coding: utf-8

import sys, heapq

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

diff = []
for i in range(n):
    diff.append(abs(t - h[i] * 0.006 - a))

print(diff.index(min(diff)) + 1)
