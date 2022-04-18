

# ======
#  Main
# ======

# --- Input ---
A, B, C, D, E, F = map(int, input().split())

# --- Calculation ---
# 1. Water: 100A, 100B
# 2. Sugar: C, D
# 3. Sugar-water: 100C/E, 100D/E
# 4. Water-sugar: 100C/E - C, 100D/E - D
# 5. Water-sugar-water: 100C/E - C - 100A, 100D/E - D - 100B
# 6. Sugar-water-water: 100C/E - 100A, 100D/E - 100B
# 7. Sugar-water-sugar: 100C/E - C + D, 100D/E - D + C
# 8. Sugar-water-sugar-water: 100C/E - C + D - 100A, 100D/E - D + C - 100B
# 9. Water-sugar-water-sugar: 100C/E - C - 100A + D, 100D/E - D - 100B + C

# --- Output ---
candidates = [
    (100 * C / E - C - 100 * A, 100 * D / E - D - 100 * B),
    (100 * C / E - 100 * A, 100 * D / E - 100 * B),
    (100 * C / E - C + D, 100 * D / E - D + C),
    (100 * C / E - C + D - 100 * A, 100 * D / E - D + C - 100 * B),
    (100 * C / E - C - 100 * A + D, 100 * D / E - D - 100 * B + C),
]
candidates = list(filter(lambda x: x[0] + x[1] <= F and x[0] >= 0.0 and x[1] >= 0.0, candidates))
candidates = list(map(lambda x: (int(round(x[0])), int(round(x[1]))), candidates))
candidate = max(candidates, key=lambda x: 100 * x[1] / (x[0] + x[1]))
print(candidate[0] + candidate[1], candidate[1])
