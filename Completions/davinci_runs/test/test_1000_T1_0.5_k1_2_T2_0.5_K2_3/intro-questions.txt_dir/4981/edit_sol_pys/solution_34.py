
import sys

def get_file_content(file_name):
    with open(file_name, 'r') as f:
        return f.read()

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
