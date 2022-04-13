import sys
import math

N,K= map(int, sys.stdin.readline().split())

if K==1:
    print(0)
elif K<=N:
    print(N-K)
else:
    print(N-math.ceil(K/2))
