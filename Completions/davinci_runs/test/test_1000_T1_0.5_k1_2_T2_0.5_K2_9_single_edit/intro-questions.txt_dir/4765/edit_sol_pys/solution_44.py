
import sys
sys.setrecursionlimit(10**6)
import itertools

n = int(input())
perk_ingredients = []

for i in range(n):
    s, b = [int(x) for x in input().split()]
    perk_ingredients.append((s, b))

perk_combinations = list(itertools.combinations(perk_ingredients, 2))

for i in range(3, n+1):
    perk_combinations.extend(list(itertools.combinations(perk_ingredients, i)))
perk_combinations = [list(x) for x in perk_combinations]
min_diff = float('inf')

for combo in perk_combinations:
    s_sum = 0
    b_sum = 0
    for ing in combo:
        s_sum += ing[0]
        b_sum += ing[1]
    diff = abs(s_sum - b_sum) + 1
    if diff < min_diff:
        min_diff = diff

print(min_diff)
