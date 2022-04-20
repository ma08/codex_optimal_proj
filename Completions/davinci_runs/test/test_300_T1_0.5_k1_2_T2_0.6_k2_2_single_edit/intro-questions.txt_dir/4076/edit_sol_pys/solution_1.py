

# Set up
h, m = map(int, input().split())

# Solve
theta_h = h * 360 / 12
theta_m = M * 360 / 60
theta_hm = theta_h - theta_m

if theta_hm < 0:
    theta_hm = 360 + theta_hm

theta_hm = theta_hm * math.pi / 180

c = math.sin(math.pi / 2 - theta_h) * math.sin(math.pi / 2 - theta_m)
c = math.sqrt(c)

# Output
print(c)
