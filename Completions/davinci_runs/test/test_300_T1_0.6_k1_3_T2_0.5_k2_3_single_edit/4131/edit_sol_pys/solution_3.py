
import sys
import collections

def main():
    n, m = map(int, sys.stdin.readline().split())

n, m = map(int, sys.stdin.readline().split())

pref_dic = collections.defaultdict(list)
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    pref_dic[p].append(City(p, y))

for p, c in sorted(pref_dic.items()):
    c.sort(key=lambda x: x.year)
    for i, city in enumerate(c):
        print('{:0>6d}{:0>6d}'.format(city.pref, i + 1))
