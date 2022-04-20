

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse=True)

# print(a)

if max(a) * (n + 1) < m:
    print(-1)
else:
    i = 0
    while m > 0:
        m -= a[i]
        i += 1
    print(i)