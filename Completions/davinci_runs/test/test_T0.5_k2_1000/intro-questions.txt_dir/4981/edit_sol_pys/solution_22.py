

# Get input
line = input().split()
order = input().upper()

# Convert to integers
nums = [int(x) for x in line]

# Sort the numbers
nums.sort()

# Print in order
for c in order:
    if c == 'A' or c == 'a':
        print(nums[0], end=' ')
    elif c == 'B' or c == 'b':
        print(nums[1], end=' ')
    else:
        print(nums[2], end=' ')
