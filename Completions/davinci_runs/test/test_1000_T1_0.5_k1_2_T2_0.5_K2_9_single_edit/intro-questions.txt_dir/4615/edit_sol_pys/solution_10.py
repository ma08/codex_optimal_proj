
# ======
#  Main
# ======

A, B, C, D, E, F = map(int, input().split())

candidates = [
    (100 * C / E - C - 100 * A, 100 * D / E - D - 100 * B),
    (100 * C / E - 100 * A, 100 * D / E - 100 * B),
    (100 * C / E - C + D, 100 * D / E - D + C),
    (100 * C / E - C + D - 100 * A, 100 * D / E - D + C - 100 * B),
    (100 * C / E - C - 100 * A + D, 100 * D / E - D - 100 * B + C),
]
candidates = list(
    filter(lambda x: x[0] + x[1] <= F and x[0] >= 0 and x[1] >= 0, candidates)
)
candidates = list(map(lambda x: (int(x[0]), int(x[1])), candidates))
candidate = max(
    candidates, key=lambda x: 100 * x[1] / (x[0] + x[1]) if x[0] + x[1] > 0 else 0
)
print(candidate[0] + candidate[1], candidate[1])
