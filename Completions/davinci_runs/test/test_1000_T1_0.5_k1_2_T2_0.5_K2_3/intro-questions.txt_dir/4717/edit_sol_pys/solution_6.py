
from itertools import permutations

x, a, b = map(int, input().split())

lst = [x, a, b]

perm = permutations(lst)

for p in perm:
    if p[0] - p[1] == p[2]:
        print(p[1])
        break
    else:
        continue
