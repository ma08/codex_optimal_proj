# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = list(map(int, input().split()))

print(sum(A))
