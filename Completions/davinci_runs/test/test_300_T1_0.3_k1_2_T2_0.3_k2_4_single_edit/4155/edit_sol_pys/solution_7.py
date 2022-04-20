
import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().strip().split()))

ans = 0
for i in range(n):
    if h[i] > ans:
        ans = h[i]

print(ans)
