import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

if a[-1] > n:
    sys.exit(-1)

s = 0
for i in range(m):
    s += a[i]

sys.exit(n - s)
