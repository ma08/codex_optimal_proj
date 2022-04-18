
import sys
import collections

n, m = map(int, sys.stdin.readline().split())

pref_dict = collections.defaultdict(list)
for _ in range(m):
    p, y = map(int, sys.stdin.readline().split())
    pref_dict[p].append((p, y))

for p, c in sorted(pref_dict.items()):
    c.sort(key=lambda x: x.year)
    for i, (p, y) in enumerate(c):
        print('{:0>6d}{:0>6d}'.format(p, i + 1))
