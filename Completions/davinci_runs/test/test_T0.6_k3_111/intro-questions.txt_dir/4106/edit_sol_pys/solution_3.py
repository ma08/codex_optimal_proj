
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]

ans = 0
for i in range(n + 1):
    if a[i] > k:
        continue
    j = m
    while j > 0 and a[i] + b[j] > k:
        j -= 1
    ans = max(ans, i + j)

print(ans)
