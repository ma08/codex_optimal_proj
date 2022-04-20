

import math

N = int(input())

if N < 10:
    print(N)
else:
    n = 1
    while n * 10 <= N:
        n *= 10
    print(N - n + 1 + math.floor(N / (2 * n)) * n)