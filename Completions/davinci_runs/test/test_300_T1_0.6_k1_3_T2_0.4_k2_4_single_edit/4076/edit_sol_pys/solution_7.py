import math


# input
[a, b, h, m] = map(int, input().split())

# degree
# clock hands coordinate
x_h = a * math.sin(math.radians(30 * h + 0.5 * m))
y_h = a * math.cos(math.radians(30 * h + 0.5 * m))
x_m = b * math.sin(math.radians(6 * m))
y_m = b * math.cos(math.radians(6 * m))

# coordinate
x = x_h - x_m
y = y_h - y_m

# output
print(math.sqrt(x ** 2 + y ** 2))
