
# SOLUTION
import sys

data = sys.stdin.read().split()
n, k, x = map(int, data[:3])
a = list(map(int, data[3:]))

if x < k:
    print(-1)
    sys.exit(0)

result = sum(a[:k])

for i in range(k, n):
    result += a[i] - a[i - k]

print(result)
