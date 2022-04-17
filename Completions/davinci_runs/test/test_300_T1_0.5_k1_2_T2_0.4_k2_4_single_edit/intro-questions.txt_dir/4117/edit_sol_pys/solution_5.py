
# coding: utf-8
# Your code here!
import numpy as np
N = int(input())
A = np.array(list(map(int,input().split())))
B = np.array(list(map(int,input().split())))
C = np.array(list(map(int,input().split())))
A = np.sort(A)
B = np.sort(B)
C = np.sort(C)
ans = 0
for b in B:
    a = np.searchsorted(A,b)
    c = np.searchsorted(C,b)
    ans += a*(N-c)
print(ans)
