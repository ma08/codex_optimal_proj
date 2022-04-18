

import sys

k, x = list(map(int, sys.stdin.readline().split()))

for i in range(k+1):
    print(x - k + 1 + i, end=" ")
