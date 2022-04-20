import math

# Get input
a, b, c = map(int, input().split())

# Calculate the area of the triangle
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Print the area
print(int(area))
