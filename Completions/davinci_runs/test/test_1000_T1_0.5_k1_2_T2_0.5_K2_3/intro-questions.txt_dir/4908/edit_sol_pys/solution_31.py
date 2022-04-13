

nums = [float(x) for x in input().split()]

if nums[2] == nums[0] + nums[1]:
    print(str(nums[0]) + " + " + str(nums[1]) + " = " + str(nums[2]))
elif nums[2] == nums[0] - nums[1]:
    print(str(nums[0]) + " - " + str(nums[1]) + " = " + str(nums[2]))
elif nums[2] == nums[0] * nums[1]:
elif nums[2] == nums[0] / nums[1]:
    print(str(nums[0]) + " / " + str(nums[1]) + " = " + str(nums[2]))
    print(str(nums[0]) + " * " + str(nums[1]) + " = " + str(nums[2]))
else:
    print("No solution")
