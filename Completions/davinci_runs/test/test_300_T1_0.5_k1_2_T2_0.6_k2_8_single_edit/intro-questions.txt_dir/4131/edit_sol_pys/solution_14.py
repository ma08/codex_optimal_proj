

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n):
    if a[i] > b[i]:
        ans += b[i]
        a[i] -= b[i]
        b[i] = 0
    else:
        ans += a[i]
        b[i] -= a[i]
        a[i] = 0

    if a[i] > 0 and b[i+1] > 0:
        b[i+1] -= min(a[i], b[i+1])
        ans += min(a[i], b[i+1])

print(ans)
