

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

if m > n * 100:
    print(-1)
    sys.exit(0)

a.sort(reverse=True)

days = 0
pages_written = 0

for i in range(len(a)):
    days += 1
    pages_written += max(0, a[i] - i)
    if pages_written >= m:
        print(days)
        sys.exit(0)

print(-1)