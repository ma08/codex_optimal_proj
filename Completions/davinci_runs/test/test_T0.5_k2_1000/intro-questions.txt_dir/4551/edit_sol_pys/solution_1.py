
# Read input and convert to integers
a, b, c, d = map(int, input().split()) 

# Calculate total weight on each side
left = a + b
right = c + d

# Determine which side is heavier
if left > right:
    print('Left')
elif left < right:
    print('Right')
else:
    print('Balanced')
