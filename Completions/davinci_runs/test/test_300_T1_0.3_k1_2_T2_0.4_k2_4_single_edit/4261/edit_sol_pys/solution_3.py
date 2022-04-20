

# Read input and convert to integers
a = int(input())
b = int(input())
c = int(input())

# Calculate amount of water in bottle 2
bottle2 = c - (a - b)

# Print result
print(max(0, bottle2))
