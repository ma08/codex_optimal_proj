n = int(input())
d = dict()
for _ in range(n):
    country, year = input().split()
    if country in d:
        d[country].append(int(year))
    else:
        d[country] = [int(year)]

q = int(input())
for _ in range(q):
    country, k = input().split()
    print(sorted(d[country])[int(k)-1])
