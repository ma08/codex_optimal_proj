
n, m = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)

i = 0
ans = 0
while i < m and a[i] <= n and n > 0:
    n -= a[i]
    ans += 1
    i += 1

if i == m:
    print(ans)
else:
    print(-1)
