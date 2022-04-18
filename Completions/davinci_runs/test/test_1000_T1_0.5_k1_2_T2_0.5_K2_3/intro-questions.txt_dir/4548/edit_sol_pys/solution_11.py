import sys
import math
from itertools import permutations

n, k = map(int, input().split())

num_list = [i + 1 for i in range(n)]

for p in permutations(num_list, n):
    if k == 0:
        for i in p:
            print(i, end=' ')
        sys.exit()

print(cost)
