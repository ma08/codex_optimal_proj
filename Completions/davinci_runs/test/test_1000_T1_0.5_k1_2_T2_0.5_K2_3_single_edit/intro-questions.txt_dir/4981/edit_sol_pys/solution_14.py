

# Get input
line = input().split() #split string into list of strings
order = input() #input string

# Convert to integers using list comprehension
nums = [int(x) for x in line] #list comprehension

# Sort the numbers using built in python function
nums.sort()

# Print in order using for loop
for c in order:
    if c == 'A':
        print(nums[0], end=' ')
    elif c == 'B':
        print(nums[1], end=' ')
    else:
        print(nums[2], end=' ')
