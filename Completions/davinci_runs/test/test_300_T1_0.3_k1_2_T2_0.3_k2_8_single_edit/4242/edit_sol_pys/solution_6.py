
import sys

# Read the input
a, b = map(int, sys.stdin.readline().split())

# Find the greatest common divisor of a and b
while b:
    a, b = b, a % b

# Print the result
print(a)
