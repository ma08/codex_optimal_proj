
n = int(input())  # number of trips
trips = []
for i in range(n):
    country, year = input().split()  # country, year of trip
    year = int(year)
    trips.append((country, year))

q = int(input())  # number of queries
queries = []
for i in range(q):
    country, k = input().split()  # country, k-th trip
    k = int(k)
    queries.append((country, k))
# print(queries)


for query in queries:
    country, k = query
    trips_to_country = [trip for trip in trips if trip[0] == country]  # trips to country
    trips_to_country.sort(key=lambda t: t[1], reverse=True)
    # print(trips_to_country)
    if k > len(trips_to_country):
        print('-1')
    else:
        print(trips_to_country[k - 1][1])
