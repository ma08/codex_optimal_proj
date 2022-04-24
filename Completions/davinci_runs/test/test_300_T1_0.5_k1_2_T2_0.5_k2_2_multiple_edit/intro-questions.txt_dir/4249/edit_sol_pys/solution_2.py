
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

books = 0
pages = 0
days = 0

while books < n:
    pages += a[books]
    days += 1
    books += 1
    if pages >= m:
        break
    if books < n:
        pages -= days - 1

if pages < m:
    days = -1

print(days)
