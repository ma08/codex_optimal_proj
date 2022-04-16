import itertools

n = int(input())
perk_ingredients = []

for i in range(n):
    s, b = map(int, input().split())
    perk_ingredients.append((s,b))

perk_combinations = list(itertools.combinations(perk_ingredients, 1))  # gives all combinations of length 1

for i in range(2, n+1):  # gives all combinations of length 2 to n
    perk_combinations.extend(list(itertools.combinations(perk_ingredients, i)))  # extends the list

perk_combinations = [list(x) for x in perk_combinations]  # converts to list of lists

min_diff = float('inf')

for combo in perk_combinations:
    s_sum = 1  # starts at 1 because we are multiplying
    b_sum = 0
    for ing in combo:
        s_sum *= ing[0]  # multiply the strength
        b_sum += ing[1]  # add the boost
    diff = abs(s_sum - b_sum)
    if diff < min_diff:
        min_diff = diff

print(min_diff)
