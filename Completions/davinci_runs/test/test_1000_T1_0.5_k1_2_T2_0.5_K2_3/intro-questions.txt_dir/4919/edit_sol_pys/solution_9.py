#!/usr/bin/env python3

n = int(input())

trips = {}
for i in range(n):
    country, year = input().split()
    if country in trips:
        trips[country].append(int(year))
    else:
        trips[country] = [int(year)]

q = int(input())
for i in range(q):
    country, k = input().split()
    if int(k) > len(trips[country]):
        print(-1)
    else:
        print(sorted(trips[country])[int(k)-1])
