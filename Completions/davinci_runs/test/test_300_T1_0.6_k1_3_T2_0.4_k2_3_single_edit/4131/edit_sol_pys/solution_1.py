# import sys
# import collections
#
# class City:
#     def __init__(self, pref, year):
#         self.pref = pref
#         self.year = year
#
# n, m = map(int, sys.stdin.readline().split())
#
# pref_dic = collections.defaultdict(list)
# for _ in range(m):
#     p, y = map(int, sys.stdin.readline().split())
#     pref_dic[p].append(City(p, y))
#
# for p, c in sorted(pref_dic.items()):
#     c.sort(key=lambda x: x.year)
#     for i, city in enumerate(c):
#         print('{:0>6d}{:0>6d}'.format(city.pref, i + 1))


import heapq

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

A.sort()
hq = []

for i in range(N):
    heapq.heappush(hq, A[i])

for b, c in BC:
    for _ in range(b):
        heapq.heappush(hq, c)
    print(heapq.heappop(hq))
