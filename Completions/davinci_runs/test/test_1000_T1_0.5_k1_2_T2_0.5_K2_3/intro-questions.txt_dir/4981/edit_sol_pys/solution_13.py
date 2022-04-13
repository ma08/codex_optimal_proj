# include <iostream>

# Get input from the user
line = raw_input().split()
order = raw_input()

# Convert to integers
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
