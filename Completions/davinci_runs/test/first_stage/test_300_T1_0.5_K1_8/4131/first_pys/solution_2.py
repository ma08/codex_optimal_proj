

import sys
from collections import defaultdict

N, M = map(int, input().split())

city_dict = defaultdict(list)
for i in range(M):
    p, y = map(int, input().split())
    city_dict[p].append(y)

for p, ys in city_dict.items():
    ys.sort()

for i in range(M):
    p, y = map(int, input().split())
    print("{:06}{:06}".format(p, city_dict[p].index(y)+1))