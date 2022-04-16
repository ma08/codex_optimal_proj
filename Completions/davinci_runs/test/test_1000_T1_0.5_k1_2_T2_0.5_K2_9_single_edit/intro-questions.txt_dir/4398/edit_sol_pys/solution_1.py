

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

ans = 0
for i in range(m):
    if i < n:
        ans += a[i]
    else:
        ans += a[n - 1]

print(ans)
