

import math

# Read input
a, b, h, m = map(int, input().split())

# Calculate the angle between the hands
angle = abs(h * 30 + m * 0.5 - m * 6)

# Calculate the distance
distance = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))

# Print the result
print(distance)