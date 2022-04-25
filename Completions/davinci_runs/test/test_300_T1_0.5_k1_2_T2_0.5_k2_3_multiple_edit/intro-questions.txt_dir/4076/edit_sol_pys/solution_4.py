import math


a, b, h, m = map(int, input().split())

theta_h = h * 360 / 12
theta_m = m * 360 / 60
theta_hm = abs(theta_h - theta_m)

if theta_hm > 180:
    theta_hm = 360 - theta_hm

theta_hm = theta_hm * math.pi / 180

c = a * a + b * b - 2 * a * b * math.cos(theta_hm)
c = math.sqrt(c)

print(c)
