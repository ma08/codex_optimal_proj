
# Set up
A, B, H, M = map(int, input().split())

# Solution
theta_h = H * 30 + M / 2
theta_m = M * 6
theta_hm = theta_h - theta_m

if theta_hm > 180:
    theta_hm = 360 - theta_hm

theta_hm = theta_hm * math.pi / 180

c = A * A + B * B - 2 * A * B * math.cos(theta_hm)
c = math.sqrt(c)

# Output
print(c)
