
import sys

n, m, c = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))
ans = 0
for _ in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    result = 0
    for i in range(m):
        result += a[i] * b[i]
    result += c
    if result > 0:
        ans += 1
print(ans)
