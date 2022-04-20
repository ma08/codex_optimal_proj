

#!/usr/bin/python3
import math

n = int(input())
b = [int(x) for x in input().split()]

a = []
for i in range(n):
    if b[i] == b[i+n]:
        a.append(b[i])
    else:
        a.append(b[i]*b[i+n])

print(*a)