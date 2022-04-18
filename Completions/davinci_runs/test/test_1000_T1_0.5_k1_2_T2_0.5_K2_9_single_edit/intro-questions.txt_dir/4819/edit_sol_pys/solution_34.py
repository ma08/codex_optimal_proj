
# Get input
nums = []
for _ in range(10):
    nums.append(int(input()))

# Get distinct numbers
nums = list(set(x % 42 for x in nums))

# Print output
print(len(nums))
