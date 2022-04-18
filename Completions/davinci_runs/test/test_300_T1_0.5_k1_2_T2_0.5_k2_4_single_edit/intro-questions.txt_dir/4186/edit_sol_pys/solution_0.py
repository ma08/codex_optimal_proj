
n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] == i + 1:
        ans += 1
        if i < n - 1:
            a[i], a[i + 1] = a[i + 1], a[i]

ans = 0
for i in d:
    ans += d[i] - 2

print(ans)
