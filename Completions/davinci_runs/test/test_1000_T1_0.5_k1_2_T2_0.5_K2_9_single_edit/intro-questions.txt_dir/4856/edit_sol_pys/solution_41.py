
nums = input().split(',')

# Reverse the numbers
num1 = nums[0][::-1]
num2 = nums[1][::-1]

# Compare them
if int(num1) > int(num2):
    print(num1)
else:
    print(num2)
