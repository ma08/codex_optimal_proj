import math

# Set up
A, B, H, M = map(int, input().split())

# Solve
theta_h = H * 360 / 12
theta_m = M * 360 / 60
theta_hm = abs(theta_h - theta_m)

theta_hm = min(theta_hm, 360 - theta_hm)

theta_hm = theta_hm * math.pi / 180

c = A * A + B * B - 2 * A * B * math.cos(theta_hm)
c = math.sqrt(c)

# Output
print(c)
