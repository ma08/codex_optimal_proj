

n, d = map(int, input().split())

# Number of inspectors
num = 0

# Tree indices
indices = list(range(1, n + 1))

# While there are still trees to inspect
while indices:
    # Get the first tree index
    tree = indices.pop(0)

    # While the tree is within range of the inspector
    while indices and indices[0] <= tree + d:
        # Remove the tree index
        indices.pop(0)
    
    # Increase the number of inspectors
    num += 1

print(num)