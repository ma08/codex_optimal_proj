
import sys

n, k, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

if sum(a) / n >= m:
    print(-1)
else:
    print(m*n - sum(a))
