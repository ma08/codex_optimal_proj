

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if sum(a) < m:
    print(-1)
else:
    days = 0
    for i in range(n):
        if a[i] >= m:
            days += 1
            break
        else:
            m -= a[i]
            days += 1
    print(days)
