nums = input().split()

#reverse the numbers
nums[0] = nums[0][::-1]
nums[1] = nums[1][::-1]

#compare them
if int(nums[0]) > int(nums[1]):
    print(int(nums[0]))
else:
    print(int(nums[1]))
