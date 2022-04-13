
import itertools

n = int(input())
park_ingredients = []

for i in range(n):
    s, b = [int(x) for x in input().split()]
    park_ingredients.append((s, b))

park_combinations = list(itertools.combinations(park_ingredients, 0))

for i in range(1, n+1):
    park_combinations.extend(list(itertools.combinations(park_ingredients, i)))

park_combinations = [list(x) for x in park_combinations]

min_diff = float('inf')

for combo in park_combinations:
    s_sum = 1
    b_sum = 0
    for ing in combo:
        s_sum *= ing[0]
        b_sum += ing[1]
    diff = abs(s_sum - b_sum)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
