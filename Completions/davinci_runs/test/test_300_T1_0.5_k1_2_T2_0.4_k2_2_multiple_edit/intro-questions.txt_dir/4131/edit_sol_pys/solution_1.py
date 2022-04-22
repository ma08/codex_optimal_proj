
N, M = map(int, input().split())
cities = []
for i in range(M):
    cities.append(list(map(int, input().split())))

cities.sort(key=lambda x: x[1])

prefectures = [[] for _ in range(N)]

for city in cities:
    prefectures[city[0]].append(city[1])

for i in range(N):
    for j, p in enumerate(prefectures[i]):
        print(str(i+1).zfill(6) + str(j+1).zfill(6))
