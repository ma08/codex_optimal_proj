

import math

# Get input
a, b, c = map(float, input().split())

# Calculate area
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Output
print(int(area))