

import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)

b = []

for i in range(n):
    b.append(a.pop(0))
    if a and a[0] == b[-1]*2:
        b.append(a.pop(0))
print(b)

print(' '.join(map(str, b)))
