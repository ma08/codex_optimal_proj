
# n, k = map(int, input().split())
import sys
# h = list(map(int, input().split()))
n, k = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
h.sort()

ans = 0
for i in range(n):
    if h[i] < k:
        ans += h[i]
        k -= h[i]
    else:
        ans += k
        k = 0
        ans += (h[i] - k) * 2  # 2倍にしている

print(ans)
