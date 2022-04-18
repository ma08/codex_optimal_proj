import sys

N, M = map(int, input().split())
city = [tuple(map(int, input().split())) for i in range(M)]

l = [[] for i in range(N)]
for i in range(M):
    l[city[i][0] - 1].append(city[i][1])

for i in range(N):
    l[i].sort()

for i in range(M):
    print("%06d%06d" % (city[i][0], l[city[i][0] - 1].index(city[i][1]) + 1))
