
# Get the numbers and sort them
nums = sorted([int(num) for num in input().split()])

# Get the difference between the first and second numbers
diff = nums[1] - nums[0]

# Print the number that would make the arithmetic progression
print(nums[2] + diff)
