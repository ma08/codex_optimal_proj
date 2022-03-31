

n, m = map(int, input().split())
cups = map(int, input().split())

pages = 0
days = 0

while pages < m:
    days += 1
    pages_today = 0
    for i in range(n):
        if cups[i] > 0:
            pages_today += cups[i] - days + 1
            if pages_today < 0:
                pages_today = 0
    pages += pages_today

if pages >= m:
    print(days)
else:
    print(-1)
