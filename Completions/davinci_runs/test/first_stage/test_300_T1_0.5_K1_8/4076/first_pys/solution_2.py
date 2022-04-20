

import math

A, B, H, M = map(int, input().split())

hour_angle = 30 * H + 0.5 * M
minute_angle = 6 * M

angle = abs(hour_angle - minute_angle)
angle = min(angle, 360 - angle)

print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle))))