# -*- coding: utf-8 -*-

N, M = map(int, input().split())
cities = []
for i in range(M):
    cities.append(list(map(int, input().split())))

cities.sort(key=lambda x: x[1])

provinces = [[] for _ in range(N+1)]

for city in cities:
    provinces[city[0]].append(city[1])

for i in range(1, N+1):
    for j in range(len(provinces[i])):
        print(str(i).zfill(6) + str(j+1).zfill(6))
