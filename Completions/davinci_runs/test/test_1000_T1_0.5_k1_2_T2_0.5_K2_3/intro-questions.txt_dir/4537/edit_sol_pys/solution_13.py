
from operator import add, sub, mul, floordiv
from itertools import permutations, product

a, b = map(int, input().split())

max = 0
for p in permutations([a, b]):
    for f in [add, sub, mul, floordiv]:
        max = f(*p) if f(*p) > max else max

print(max)
