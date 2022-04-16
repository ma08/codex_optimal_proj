

from operator import add, sub, mul, truediv
from itertools import permutations

a, b = map(int, input().split())

max = 0
for p in permutations([a, b]):
    for f in [add, sub, mul, truediv]:
        max = f(*p) if f(*p) > max else max

print(max)
