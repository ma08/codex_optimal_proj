

N, M = map(int, input().split())
prefectures = [0] * (N + 1)
cities = []
for i in range(M):
    p, y = map(int, input().split())
    prefectures[p] += 1
    cities.append([p, y, i])

for i in range(1, N + 1):
    prefectures[i] += prefectures[i - 1]

cities.sort(key=lambda x: (x[0], x[1]))

for i in range(M):
    p, y, index = cities[i]
    prefecture = str(p).zfill(6)
    city = str(prefectures[p]).zfill(6)
    print(prefecture + city)