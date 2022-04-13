# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10 ** 7)


# =====
#  入力
# =====

A, B, C, D, E, F = map(int, input().split())

# =====
#  計算
# =====

# --- Output ---
candidates = [
    (100 * C / E - C - A, 100 * D / E - D - B),
    (100 * C / E - A, 100 * D / E - B),
    (100 * C / E - C + D, 100 * D / E - D + C),
    (100 * C / E - C + D - A, 100 * D / E - D + C - B),
    (100 * C / E - C - A + D, 100 * D / E - D - B + C),
]
candidates = list(filter(lambda x: x[0] + x[1] <= F and x[0] >= 0 and x[1] >= 0, candidates))
candidates = list(map(lambda x: (round(x[0]), round(x[1])), candidates))
candidates = list(map(lambda x: (int(x[0]), int(x[1])), candidates))
candidate = max(candidates, key=lambda x: 100 * x[1] / (x[0] + x[1]))
print(candidate[0] + candidate[1], candidate[1])
