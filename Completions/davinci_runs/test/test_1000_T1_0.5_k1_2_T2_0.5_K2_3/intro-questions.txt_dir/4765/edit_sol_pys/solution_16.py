

def get_min_diff(perk_ingredient, n):
    import itertools
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
    return min_diff


n = int(input().strip())
perk_ingredient = []
for _ in range(n):
    s, b = [int(x) for x in input().strip().split()]
    perk_ingredient.append((s, b))

print(get_min_diff(perk_ingredient, n))
