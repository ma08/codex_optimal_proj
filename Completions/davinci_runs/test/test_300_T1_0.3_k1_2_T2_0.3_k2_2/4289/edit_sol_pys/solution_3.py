# coding: utf-8

import math

N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

TEMP = []
for i in range(N):
    TEMP.append(T - H[i] * 0.006)

TEMP_DIFF = []
for i in range(N):
    TEMP_DIFF.append(abs(TEMP[i] - A))

print(TEMP_DIFF.index(min(TEMP_DIFF)) + 1)
