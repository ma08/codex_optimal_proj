
from operator import add, sub, mul, truediv
from itertools import permutations, product

a, b = map(int, input().split())

maximum = 0
for p in permutations([a, b]):
    for f in [add, sub, mul, truediv]:
        maximum = f(*p) if f(*p) > maximum else maximum

print(maximum)
