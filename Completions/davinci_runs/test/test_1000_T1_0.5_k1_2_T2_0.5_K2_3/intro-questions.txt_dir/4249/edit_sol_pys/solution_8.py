

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

cups = 0
pages = 0
days = 0
pages_per_day = 0
while cups < n:
    pages_per_day += a[cups]
    cups += 1
    if pages_per_day >= m and cups < n:
        pages -= days
        pages_per_day = 0
        days -= 1
    else:
    pages += a[cups]
    days += 1

if pages < m:
    days = -1

print(days)
