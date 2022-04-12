

# =============
#  Main Method
# =============

# --- Input ---
A, B, C, D, E, F = map(int, input().split())

# --- Calculation ---
# 1. Water: A, B
# 2. Sugar: C, D
# 3. Sugar-water: C/E, D/E
# 4. Water-sugar: C/E - C, D/E - D
# 5. Water-sugar-water: C/E - C - A, D/E - D - B
# 6. Sugar-water-water: C/E - A, D/E - B
# 7. Sugar-water-sugar: C/E - C + D, D/E - D + C
# 8. Sugar-water-sugar-water: C/E - C + D - A, D/E - D + C - B
# 9. Water-sugar-water-sugar: C/E - C - A + D, D/E - D - B + C

# --- Output ---
candidates = [
    (C / E - C - A, D / E - D - B),
    (C / E - A, D / E - B),
    (C / E - C + D, D / E - D + C),
    (C / E - C + D - A, D / E - D + C - B),
    (C / E - C - A + D, D / E - D - B + C),
]
candidates = list(filter(lambda x: x[0] + x[1] <= F and x[0] >= 0 and x[1] >= 0, candidates))
candidates = list(map(lambda x: (round(x[0]), round(x[1])), candidates))
candidates = list(map(lambda x: (int(x[0]), int(x[1])), candidates))
candidate = max(candidates, key=lambda x: 100 * x[1] / (x[0] + x[1]))
print(candidate[0] + candidate[1], candidate[1])
