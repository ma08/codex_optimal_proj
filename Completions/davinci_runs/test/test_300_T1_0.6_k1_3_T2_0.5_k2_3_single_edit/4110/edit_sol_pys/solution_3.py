
import sys

n, k = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

a.sort(reverse=True)
print(a[k - 1])

if g > 0:
    n += (g + (i + 1) * 100 - 1) // ((i + 1) * 100)

print(n)
