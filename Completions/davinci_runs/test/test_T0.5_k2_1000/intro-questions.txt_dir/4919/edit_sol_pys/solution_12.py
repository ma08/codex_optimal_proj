n = int(input().strip())

trips = {}
for i in range(n):
    country, year = input().strip().split()
    if country in trips:
        trips[country].append(int(year))
    else:
        trips[country] = [int(year)]

q = int(input().strip())
for i in range(q):
    country, k = input().strip().split()
    print(sorted(trips[country])[int(k)-1])
