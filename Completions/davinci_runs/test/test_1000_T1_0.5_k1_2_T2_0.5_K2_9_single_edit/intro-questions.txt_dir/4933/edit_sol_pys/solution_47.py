
# Get the numbers
nums = list(map(int, input().split()))

# Sort the numbers
nums.sort()

# Get the difference between the first and second number
diff = nums[1] - nums[0]

# Print the number that would make the arithmetic progression
print(nums[2] + diff)
