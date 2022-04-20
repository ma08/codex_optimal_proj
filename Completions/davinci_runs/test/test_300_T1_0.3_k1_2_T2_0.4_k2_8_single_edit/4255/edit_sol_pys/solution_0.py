

# Get input from user
a, b, c = map(int, input('Enter the sides of the triangle: ').split())

# Calculate the area of the triangle using Heron's formula
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

# Print the area of the triangle
print('The area of the triangle is: ', int(area))
