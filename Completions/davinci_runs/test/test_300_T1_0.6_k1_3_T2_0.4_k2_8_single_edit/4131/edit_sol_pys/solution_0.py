
import sys
import collections

class City:
    def __init__(self, pref, year, id):
        self.pref = pref
        self.id = id
        self.year = year

n, m = map(int, sys.stdin.readline().split())

id_dic = {}
pref_dic = collections.defaultdict(list)
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    id_dic[m] = City(p, y, m)
    pref_dic[p].append(id_dic[m])

for p, c in sorted(pref_dic.items()):
    c.sort(key=lambda x: x.year)
    for i, city in enumerate(c):
        print('{:0>6d}{:0>6d}'.format(city.pref, i + 1))
