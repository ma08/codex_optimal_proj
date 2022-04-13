#!/usr/bin/env python3

import itertools

n = int(input())
ingredient = []

for i in range(n):
    s, b = [int(x) for x in input().split()]
    ingredient.append((s, b))

combinations = list(itertools.combinations(ingredient, 1))

for i in range(2, n+1):
    combinations.extend(list(itertools.combinations(ingredient, i)))

combinations = [list(x) for x in combinations]

min_diff = float('inf')

for combo in combinations:
    s_sum = 1
    b_sum = 0
    for ing in combo:
        s_sum *= ing[0]
        b_sum += ing[1]
    diff = abs(s_sum - b_sum)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
