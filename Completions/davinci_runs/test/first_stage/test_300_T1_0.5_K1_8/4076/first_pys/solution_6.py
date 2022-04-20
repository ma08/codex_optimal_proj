

# a = 3
# b = 4
# h = 9
# m = 0
# theta_h = (360/12)*h + (360/12)*(m/60)
# theta_m = (360/60)*m
# print(theta_h)
# print(theta_m)
# theta = abs(theta_h - theta_m)
# print(theta)
# print(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))

a, b, h, m = map(int, input().split())
theta_h = (360/12)*h + (360/12)*(m/60)
theta_m = (360/60)*m
theta = abs(theta_h - theta_m)
print(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))