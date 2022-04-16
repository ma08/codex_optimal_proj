
from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

comb = combinations(L, 3)

count = 0
for c in comb:
    if sum(c[:2]) > c[2] and sum(c[1:]) > c[0] and sum(c[::2]) > c[1]:
        count += 1

print(count)
