

# Read input and convert to integers
a, b, c, d = map(int, input().split()) # the map function takes the input and splits it by the spaces, and then converts it to an integer. This is then stored in the variables a, b, c and d.

# Calculate total weight on each side.
left = a + b # the left side is the sum of a and b
right = c + d # the right side is the sum of c and d

# Determine which side is heavier
if left > right: # if the left side is heavier
    print('Left')
elif left < right: # if the right side is heavier
    print('Right')
else: # if the sides are equal
    print('Balanced')
