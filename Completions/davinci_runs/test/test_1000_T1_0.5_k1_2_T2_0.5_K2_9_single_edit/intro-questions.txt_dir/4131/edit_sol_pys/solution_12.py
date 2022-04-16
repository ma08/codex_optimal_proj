
N, M = map(int, input().split())
prefectures = [[] for _ in range(N+1)]
for i in range(M):
    prefecture, city = map(int, input().split())
    prefectures[prefecture].append(city)

for i in range(1, N+1):
    prefectures[i].sort()

for i in range(1, N+1):
    for j in range(len(prefectures[i])):
        print(str(i).zfill(6) + str(j+1).zfill(6))
