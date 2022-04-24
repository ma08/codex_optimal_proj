

N, M = map(int, input().split())
cities = []
for i in range(M):
    cities.append(list(map(int, input().split())))
cities.sort(key=lambda x: x[1])

prefectures = [[] for _ in range(N)]

for city in cities:
    prefectures[city[0]-1].append(city[1])

for i in range(N):
    for j in range(len(prefectures[i])):
        print(str(i).zfill(6) + str(j+1).zfill(6))
