
# Read input
a, b, c = map(int, input().split())

# Calculate total weight
left = a
right = b
center = c

# Determine which side is heaviest
if left > right:
    print('Left')
    print('Right')
elif left < right:
elif center > left and center > right:
    print('center')
else:
    print('Balanced')
