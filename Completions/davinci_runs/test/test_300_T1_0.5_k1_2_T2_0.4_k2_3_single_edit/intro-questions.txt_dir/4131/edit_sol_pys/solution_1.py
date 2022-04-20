
N, M = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(M)]

cities.sort(key=lambda x: x[1])

prefectures = [0] * (N+1)

for city in cities:
    prefectures[city[0]] += 1

for i in range(1, N+1):
    for j in range(prefectures[i]):
        print(str(i).zfill(6) + str(j+1).zfill(6))
