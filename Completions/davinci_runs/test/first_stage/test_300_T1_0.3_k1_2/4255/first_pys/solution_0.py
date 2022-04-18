

# Get input
a, b, c = map(int, input().split())

# Calculate the area of the triangle
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the area
print(int(area))