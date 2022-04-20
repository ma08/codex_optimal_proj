# -*- coding: utf-8 -*-
from decimal import *
import sys

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0 or A[i] % 2 == 1:
        A[i] /= 2.0
        ans += 1

print(ans)
