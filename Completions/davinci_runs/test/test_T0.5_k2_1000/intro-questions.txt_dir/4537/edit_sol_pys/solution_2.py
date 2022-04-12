
from operator import add, sub, mul
from itertools import permutations

a, b = map(int, input().split())

maximum = 0
for p in permutations([a, b]):
    for f in [add, sub, mul]:
        maximum = f(*p) if f(*p) > maximum else maximum

print(max)
