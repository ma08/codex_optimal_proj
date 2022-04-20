

# Read input from user
a, b, c = map(int, input().split()) # a, b, c are integers

# Calculate amount of water in bottle 2 (c - (a - b))
bottle2 = c - (a - b) # bottle2 is an integer

# Print result
print(max(0, bottle2))
