

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

cups = 0
pages = 1
days = 0

while cups < n:
    pages += a[cups]
    days += 1
    cups += 1
    if pages >= m:
        break
    if cups < n:
        pages -= days

if pages < m:
    days = -1

print(days)
