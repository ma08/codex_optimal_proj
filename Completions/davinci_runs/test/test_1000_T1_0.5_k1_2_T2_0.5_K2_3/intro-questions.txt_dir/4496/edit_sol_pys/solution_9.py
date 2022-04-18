
import sys
import math

N, M = map(int, sys.stdin.readline().split())

if N == 1:
    print(M)
else:
    print(M - math.ceil(M / 2))
