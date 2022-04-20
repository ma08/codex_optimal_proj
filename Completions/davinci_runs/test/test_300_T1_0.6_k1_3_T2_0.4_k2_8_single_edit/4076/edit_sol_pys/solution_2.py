
import math

A, B, H, M = map(int, input().split())

rad_h = 2 * math.pi * (H / 12 + M / 60 / 12)
rad_m = 2 * math.pi * (M / 60)

rad = abs(rad_h - rad_m) % (2 * math.pi)

print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)))
