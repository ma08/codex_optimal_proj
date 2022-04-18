

n = int(input())
d = dict()
for _ in range(n):
    country, year = input().split()
    year = int(year)
    if country in d:
        d[country].append(year)
    else:
        d[country] = [year]

q = int(input())
for _ in range(q):
    country, k = input().split()
    k = int(k)
    if k <= len(d[country]):
        print(sorted(d[country])[k-1])
    else:
        print("none")
