n = int(input()) # number of trips

trips = {} # dictionary of trips
for i in range(n):
    country, year = input().split()
    if country in trips:
        trips[country].append(int(year))
    else:
        trips[country] = [int(year)]

q = int(input()) # number of queries
for i in range(q):
    country, k = input().split()
    print(sorted(trips[country])[int(k)-1]) # print the kth year of the country
