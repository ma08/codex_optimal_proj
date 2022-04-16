
# Read input
a, b, c, d = map(int, input().split())  # Reads 4 integers from stdin

# Calculate total weight on each side
left = a + b
right = c + d

# Determine which side is heavier
if left > right:
    print('Left')  # Prints 'Left'
elif left < right:
    print('Right')  # Prints 'Right'
else:
    print('Balanced')  # Prints 'Balanced'
