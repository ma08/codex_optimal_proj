"""

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
    print(trips_to_country[k - 1][1])
"""


def f(n):
    if n <= 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)


n = int(input())
print(f(n))
