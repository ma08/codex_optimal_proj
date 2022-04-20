

n = int(input())
arr = [int(i) for i in input().split()]

# Create a prefix sum array
ps = [arr[0]]
for i in range(1, n):
    ps.append(ps[-1] + arr[i])

# Create a dictionary of all sums to the indices of their occurences
sums = {}
for i in range(n):
    if ps[i] in sums:
        sums[ps[i]].append(i)
    else:
        sums[ps[i]] = [i]

# Create a dictionary of all sums to the number of times they occur
sums_count = {}
for key in sums:
    sums_count[key] = len(sums[key])

# Create a dictionary of all sums to the number of blocks they can create
sums_blocks = {}
for key in sums_count:
    sums_blocks[key] = sums_count[key]
    if key != 0:
        sums_blocks[key] -= 1

# Create a list of all sums that can create blocks
sums_blocks_keys = []
for key in sums_blocks:
    if sums_blocks[key] > 0:
        sums_blocks_keys.append(key)

# Sort the list of all sums that can create blocks
sums_blocks_keys.sort(reverse=True)

# Create a list of all blocks
blocks = []
for key in sums_blocks_keys:
    for i in range(sums_blocks[key]):
        blocks.append(sums[key][i+1] - sums[key][i])

# Sort the list of all blocks
blocks.sort(reverse=True)

# Create a list of all possible indices
indices = []
for i in range(n):
    indices.append(i)

# Create a list of all blocks that don't overlap
non_overlapping_blocks = []
for block in blocks:
    for i in range(len(indices) - block + 1):
        non_overlapping_blocks.append(indices[i:i+block])
        indices = indices[i+block:]
        break

# Print the number of blocks
print(len(non_overlapping_blocks))

# Print the blocks
for block in non_overlapping_blocks:
    print(block[0]+1, block[-1]+1)