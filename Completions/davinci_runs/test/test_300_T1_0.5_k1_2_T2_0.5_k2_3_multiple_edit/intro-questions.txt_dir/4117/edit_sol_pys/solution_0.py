
from itertools import combinations, permutations

N = int(input())
L = list(map(int, input().split()))

comb = permutations(L, 3)

count = 0
for c in list(comb):
    if c[0] + c[1] > c[2] and c[1] + c[2] > c[0] and c[2] + c[0] > c[1] and c[0] != c[1] and c[1] != c[2]:
        count += 1

print(count)
