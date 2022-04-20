

import math

A, B, H, M = map(int, input().split())

if H == 12:
    H = 0

if M == 60:
    M = 0

if H == 0 and M == 0:
    ans = 0
else:
    H_angle = H * 30 + M * 0.5
    M_angle = M * 6

    angle = abs(H_angle - M_angle)

    if angle > 180:
        angle = 360 - angle

    ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(angle)))

print(ans)