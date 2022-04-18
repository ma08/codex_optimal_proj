nums = input().split() # split the input into a list

# Reverse the numbers
nums[0] = nums[0][::-1] # reverse the first number
nums[1] = nums[1][::-1] # reverse the second number

# Compare them and print the higher number
if int(nums[0]) > int(nums[1]): # if the first number is greater than the second number
    print(nums[0])
else: # if the second number is greater than the first number
    print(nums[1])
