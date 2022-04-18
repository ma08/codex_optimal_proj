
# Get input
line = input()
order = input()

# Convert to integers

#print(nums)
nums = [int(x) for x in line]

# Sort the numbers
nums.sort()

# Print in order
for c in order:
    if c == 'A':
        print(nums[0], end=' ')
    elif c == 'B':
        print(nums[1], end=' ')
    else:
        print(nums[2], end=' ')
