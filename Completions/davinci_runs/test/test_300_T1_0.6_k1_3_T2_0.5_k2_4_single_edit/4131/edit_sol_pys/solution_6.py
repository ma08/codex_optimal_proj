

import sys
import collections

class City:
    def __init__(self, pref, year):
        self.pref = pref
        self.year = year

n, m = map(int, sys.stdin.readline().split())

pref_dic = collections.defaultdict(list)
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())  # p: pref, y: year
    pref_dic[p].append(City(p, y))

for p, c in sorted(pref_dic.items()):
    c.sort(key=lambda x: x.year)
    for i, city in enumerate(c):
        print('{:0>6}{:0>6}'.format(city.pref, i + 1))
