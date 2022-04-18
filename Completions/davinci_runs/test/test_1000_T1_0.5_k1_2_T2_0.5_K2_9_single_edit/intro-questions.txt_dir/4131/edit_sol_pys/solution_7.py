import itertools

N, M = map(int, input().split())
cities = []
for i in range(M):
    cities.append(list(map(int, input().split())))

cities.sort(key=lambda x: x[1])

prefectures = [[] for _ in range(N+1)]

for city in cities:
    prefectures[city[0]].append(city[1])

for p in prefectures:
    for i, j in enumerate(p):
        print(str(prefectures.index(p)).zfill(6) + str(i+1).zfill(6))
