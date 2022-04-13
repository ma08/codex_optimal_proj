import sys

n = int(sys.stdin.readline())
a = sorted(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(n):
    if a[i] < i + 1:
        ans += 1
print(ans)
