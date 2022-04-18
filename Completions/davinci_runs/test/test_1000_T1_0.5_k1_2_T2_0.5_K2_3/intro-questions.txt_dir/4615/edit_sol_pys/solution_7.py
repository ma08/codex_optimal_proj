

# ======
#  Main
# ======

# --- Input ---
A, B, C, D, E, F = map(int, input().split())

# --- Calculation ---
# 1. Water: A, B
# 2. Sugar: C, D
# 3. Sugar-water: 100C/E, 100D/E
# 4. Water-sugar: 100C/E - C, 100D/E - D
# 5. Water-sugar-water: 100C/E - C - A, 100D/E - D - B
# 6. Sugar-water-water: 100C/E - A, 100D/E - B
# 7. Sugar-water-sugar: 100C/E - C + D, 100D/E - D + C
# 8. Sugar-water-sugar-water: 100C/E - C + D - A, 100D/E - D + C - B
# 9. Water-sugar-water-sugar: 100C/E - C - A + D, 100D/E - D - B + C

# --- Output ---
candidates = [
    (100 * C / E - C - A, 100 * D / E - D - B),
    (100 * C / E - A, 100 * D / E - B),
    (100 * C / E - C + D, 100 * D / E - D + C),
    (100 * C / E - C + D - A, 100 * D / E - D + C - B),
    (100 * C / E - C - A + D, 100 * D / E - D - B + C),
]
candidates = list(
    filter(lambda x: x[0] + x[1] <= F and x[0] >= 0 and x[1] >= 0, candidates))
candidates = list(
    map(lambda x: (round(x[0]), round(x[1])), candidates))
candidates = list(
    map(lambda x: (int(x[0]), int(x[1])), candidates))
candidate = max(
    candidates, key=lambda x: 100 * x[1] / (x[0] + x[1]))
print(candidate[0] + candidate[1], candidate[1])
