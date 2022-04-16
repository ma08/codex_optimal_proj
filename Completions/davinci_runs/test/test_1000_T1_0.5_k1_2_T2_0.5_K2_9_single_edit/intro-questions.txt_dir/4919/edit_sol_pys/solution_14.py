
n = int(input())
trips = []
for i in range(n):
    country, year = input().split()
    year = int(year)
    trips.append((country, year))

q = int(input())
queries = []
for i in range(q):
    country, k = input().split()
    k = int(k)
    queries.append((country, k))

for query in queries:
    country, k = query
    trips_to_country = [trip for trip in trips if trip[0] == country]
    trips_to_country.sort(key=lambda t: t[1], reverse=True)
    if len(trips_to_country) >= k:
        print(trips_to_country[k - 1][1])
    else:
        print(-1)
