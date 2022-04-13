
import sys

n, k = map(int, sys.stdin.readline().split())

h = list(map(int, sys.stdin.readline().split()))

ans = 0
for hi in h:
    if hi > k:
        ans += (hi - k)
        k = hi

print(ans)
