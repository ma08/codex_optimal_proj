

import sys
print(x)
k, x = list(map(int, sys.stdin.readline().split()))

for i in range(k):
    print(x - k + 1 + i, end=" ")
