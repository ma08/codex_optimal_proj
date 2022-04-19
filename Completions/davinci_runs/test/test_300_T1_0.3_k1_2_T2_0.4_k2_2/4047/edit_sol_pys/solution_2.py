n = int(input())
a = list(map(int, input().split()))


a.sort()

ans = 0
for i in range(n - 1):
    if a[i + 1] - a[i] > 1:
        ans += a[i + 1] - a[i] - 1

ans = 0
for i in range(1, n):
    if x[i] - x[i-1] > 1:
        ans += x[i] - x[i-1] - 1

print(ans)
