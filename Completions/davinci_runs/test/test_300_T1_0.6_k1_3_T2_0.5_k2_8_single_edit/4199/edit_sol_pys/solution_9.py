import sys

n, k = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0

for i in h:
    if i >= k:
        ans += 1
print(ans)
