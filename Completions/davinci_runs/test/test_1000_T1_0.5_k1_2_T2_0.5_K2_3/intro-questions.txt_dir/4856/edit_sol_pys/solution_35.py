
nums = input('Enter two numbers: ').split()

# Reverse the number
nums[0] = nums[0][::-1]
nums[1] = nums[1][::-1]

# Compare them
if int(nums[0]) > int(nums[1]):
    print('The larger number is: ', nums[0])
else:
    print('The larger number is: ', nums[1])
