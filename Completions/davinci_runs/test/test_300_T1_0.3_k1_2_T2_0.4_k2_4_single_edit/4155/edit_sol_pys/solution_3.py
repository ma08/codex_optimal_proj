

import sys
n = int(sys.stdin.readline().rstrip())
h = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0
for i in range(n):
    if h[i] != 0:
        for j in range(i):
            h[j] += 1
        for j in range(i + 1, n):
            h[j] += 1
        count += 1
print(count)
