

import sys

n = int(input())
a = [int(s) for s in input().split()]

b = [a[i] for i in range(n)]
b.reverse()

print(*b)
