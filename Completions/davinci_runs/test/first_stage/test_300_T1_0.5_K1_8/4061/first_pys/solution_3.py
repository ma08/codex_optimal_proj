

#!/usr/bin/python3

# import sys
# # For faster input
# input = sys.stdin.readline

# Read input
s = input()
t = input()

# Create a list of indices of characters in t from s
indices = []
for c in t:
    indices.append(s.find(c))
    s = s[s.find(c)+1:]

# Remove all -1 indices
indices = list(filter(lambda x: x != -1, indices))

# Remove all continuous indices
i = 0
while i < len(indices)-1:
    if indices[i] + 1 == indices[i+1]:
        del indices[i]
    else:
        i += 1

# Remove all continuous indices
i = 0
while i < len(indices)-1:
    if indices[i] + 1 == indices[i+1]:
        del indices[i]
    else:
        i += 1

# If there are no indices, print 0
if len(indices) == 0:
    print(0)
else:
    # Find the maximum length of all continuous substrings
    i = 0
    max_length = 0
    while i < len(indices)-1:
        length = indices[i+1] - indices[i] - 1
        if length > max_length:
            max_length = length
        i += 1
    print(max_length)