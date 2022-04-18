

n = int(input())
a = list(map(int, input().split()))

a.sort()

if n % 2 == 0:
    ans = 0
    for i in range(n):
        if i % 2 == 0:
            ans += a[i]
        else:
            ans -= a[i]
else:
    ans = a[0]
    for i in range(1, n):
        if i % 2 == 1:
            ans += a[i]
        else:
            ans -= a[i]

print(ans)
