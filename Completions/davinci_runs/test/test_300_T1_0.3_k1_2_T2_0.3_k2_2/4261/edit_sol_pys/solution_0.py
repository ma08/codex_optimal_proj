

# Read input and convert to int
a, b, c = map(int, input().split()) 

# Calculate amount of water in bottle 2
bottle2 = c - (a - b)

# Print result
print(max(0, bottle2))
