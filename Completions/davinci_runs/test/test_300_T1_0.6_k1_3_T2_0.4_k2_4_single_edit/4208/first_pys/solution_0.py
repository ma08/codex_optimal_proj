

# I/O
n = int(input())
left = input()
right = input()

# Solution

# Create a list of all possible left/right pairs
pairs = []
for i in range(n):
    for j in range(n):
        pairs.append((i+1, j+1))

# Filter out pairs where colors don't match
for i in range(n):
    if left[i] != "?" and right[i] != "?":
        if left[i] != right[i]:
            pairs = [pair for pair in pairs if pair[0] != i+1 and pair[1] != i+1]

# Filter out pairs where left boots repeat
left = [pair[0] for pair in pairs]
dups = [i for i in left if left.count(i) > 1]
pairs = [pair for pair in pairs if pair[0] not in dups]

# Filter out pairs where right boots repeat
right = [pair[1] for pair in pairs]
dups = [i for i in right if right.count(i) > 1]
pairs = [pair for pair in pairs if pair[1] not in dups]

# Print pairs
print(len(pairs))
for pair in pairs:
    print(pair[0], pair[1])