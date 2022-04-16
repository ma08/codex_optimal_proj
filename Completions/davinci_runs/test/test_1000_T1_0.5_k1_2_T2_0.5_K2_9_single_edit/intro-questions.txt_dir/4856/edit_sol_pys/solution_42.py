
nums = input().split()

# Reverse the numbers
nums[0] = int(nums[0][::-1])
nums[1] = int(nums[1][::-1])

# Compare them
if nums[0] > nums[1]:
    print(nums[0])
else:
    print(nums[1])
