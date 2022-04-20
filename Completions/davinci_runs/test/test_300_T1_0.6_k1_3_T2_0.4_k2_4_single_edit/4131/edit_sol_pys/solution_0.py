
import sys
import collections

class City:
    def __init__(self, pref, year, id):
        self.pref = pref
        self.id = id
        self.year = year

city_list = [None] * m
n, m = map(int, sys.stdin.readline().split())

prefs = collections.defaultdict(list)
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    city_list[_] = City(p, y, _)
    prefs[p].append(city_list[_])

for p, cities in sorted(prefs.items()):
    cities.sort(key=lambda x: x.year)
    for i, city in enumerate(cities):
        city_list[city.id] = '{:0>6d}{:0>6d}'.format(city.pref, i + 1)

for city in city_list:
    print(city)
