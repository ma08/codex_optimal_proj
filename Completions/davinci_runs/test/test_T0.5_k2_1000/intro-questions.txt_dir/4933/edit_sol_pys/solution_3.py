
# Get the number
nums = [int(num) for num in input().split()]

# Sort the number
nums.sort()

# Get the difference between the first and second number
diff = nums[1] - nums[0]

# Print the number that would make the arithmetic progression
print(nums[2] + diff)
