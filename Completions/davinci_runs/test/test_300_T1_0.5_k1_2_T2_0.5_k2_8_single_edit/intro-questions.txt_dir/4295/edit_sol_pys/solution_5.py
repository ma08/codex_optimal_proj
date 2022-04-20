
import math

N, A, B = map(int, input().split())
n = math.floor(N / (A + B))
r = N % (A + B)

if N % K == 0:
    print(0)
else:
    print(1)
