
nums = input().split() #inputs two numbers

# Reverse the number 
nums[0] = nums[0][::-1] #reverses the first number
nums[1] = nums[1][::-1] #reverses the second number

# Compare them 
if int(nums[0]) > int(nums[1]): #if the first number is greater than the second number
    print(nums[0]) #print the first number
else:
    print(nums[1]) #print the second number
