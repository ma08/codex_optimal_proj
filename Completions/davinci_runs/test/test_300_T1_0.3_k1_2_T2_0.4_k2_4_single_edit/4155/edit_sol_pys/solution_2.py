import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        ans += a[i] * a[j]

print(ans)


n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    if h[i] < h[i-1]:
        ans += h[i-1] - h[i]

print(ans)
