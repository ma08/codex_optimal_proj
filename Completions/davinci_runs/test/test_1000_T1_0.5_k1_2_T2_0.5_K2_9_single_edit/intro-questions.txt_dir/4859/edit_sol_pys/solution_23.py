
from itertools import product
b, d, c, l = map(int, input().split())

for i, j, k in product(range(l//b + 1), range(l//d + 1), range(l//c + 1)):
    if i*b + j*d + k*c == l:
        print(i, j, k)
