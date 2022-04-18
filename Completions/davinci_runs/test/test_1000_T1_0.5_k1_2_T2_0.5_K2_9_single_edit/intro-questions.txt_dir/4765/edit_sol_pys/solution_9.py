
import itertools

n = int(input())  # number of ingredients
perk_ingredients = []

for i in range(n):
    s, b = [int(x) for x in input().split()]  # s: sweetness, b: bitterness
    perk_ingredients.append((s, b))  # append as tuple

perk_combinations = list(itertools.combinations(perk_ingredients, 1))  # combinations of 1 ingredient

for i in range(2, n + 1):
    perk_combinations.extend(list(itertools.combinations(perk_ingredients, i)))  # combinations of 2,3,..n ingredients

perk_combinations = [list(x) for x in perk_combinations]  # convert tuples to lists

min_diff = float('inf')

for combo in perk_combinations:
    s_sum = 1  # sweetness
    b_sum = 0  # bitterness
    for ing in combo:
        s_sum *= ing[0]  # multiply sweetness
        b_sum += ing[1]  # add bitterness
    diff = abs(s_sum - b_sum)  # difference
    if diff < min_diff:
        min_diff = diff

print(min_diff)
