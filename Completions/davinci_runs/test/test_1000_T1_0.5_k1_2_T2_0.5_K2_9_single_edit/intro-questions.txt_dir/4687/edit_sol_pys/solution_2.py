

import sys

N, K = map(int, input().split())

for i in range(N):
    a, b = map(int, input().split())
    if K <= b:
        print(a)
        sys.exit()
    else:

print(0)
        K -= b
