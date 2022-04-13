import sys

import itertools

n = int(sys.stdin.readline())
perk_ingredient = []

for i in range(n):
    s, b = [int(x) for x in sys.stdin.readline().split()]
    perk_ingredient.append((s, b))

perk_combinations = list(itertools.combinations(perk_ingredient, 1))

for i in range(2, n+1):
    perk_combinations.extend(list(itertools.combinations(perk_ingredient, i)))

perk_combinations = [list(x) for x in perk_combinations]

min_diff = float('inf')

for combo in perk_combinations:
    s_sum = 1
    b_sum = 0
    for ing in combo:
        s_sum *= ing[0]
        b_sum += ing[1]
    diff = abs(s_sum - b_sum)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
