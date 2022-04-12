

# Get input
line = input().split() # ['1', '2', '3']
order = input() # 'ABC'

# Convert to integers
nums = [int(x) for x in line] # [1, 2, 3]

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
