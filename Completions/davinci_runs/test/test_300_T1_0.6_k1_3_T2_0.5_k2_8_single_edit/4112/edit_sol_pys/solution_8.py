

# SOLUTION
import sys, heapq

n, k, x = map(int, sys.stdin.read().split())
a = list(map(int, sys.stdin.read().split()))

if x < k or k == 1:
    print(-1)
    sys.exit(0)

result = sum(a[:k])

for i in range(k, n):
    result += a[i] - a[i - k]

print(result)
