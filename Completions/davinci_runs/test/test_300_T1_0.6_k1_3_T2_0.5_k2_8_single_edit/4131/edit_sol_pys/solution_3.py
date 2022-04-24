# -*- coding: utf-8 -*-


N = int(input())
city = [tuple(map(int, input().split())) for i in range(N)]

l = [[] for i in range(100)]
for i in range(N):
    l[city[i][0] - 1].append(city[i][1])

for i in range(100):
    l[i].sort()

for i in range(N):
    print("%06d%06d" % (city[i][0], l[city[i][0] - 1].index(city[i][1]) + 1))
