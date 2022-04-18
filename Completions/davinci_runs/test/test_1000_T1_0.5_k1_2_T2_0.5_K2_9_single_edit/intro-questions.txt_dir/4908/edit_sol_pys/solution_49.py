
nums = list(map(int, input().split()))

if nums[0] + nums[1] == nums[2]:
    print(str(nums[0]) + '+' + str(nums[1]) + '=' + str(nums[2]))
elif nums[0] - nums[1] == nums[2]:
    print(str(nums[0]) + '-' + str(nums[1]) + '=' + str(nums[2]))
elif nums[0] * nums[1] == nums[2]:
    print(str(nums[0]) + '*' + str(nums[1]) + '=' + str(nums[2]))
elif nums[0] / nums[1] == nums[2]:
    print(str(nums[0]) + '/' + str(nums[1]) + '=' + str(nums[2]))
elif nums[0] == nums[1] + nums[2]:
    print(str(nums[0]) + '=' + str(nums[1]) + '+' + str(nums[2]))
elif nums[0] == nums[1] - nums[2]:
    print(str(nums[0]) + '=' + str(nums[1]) + '-' + str(nums[2]))
elif nums[0] == nums[1] * nums[2]:
    print(str(nums[0]) + '=' + str(nums[1]) + '*' + str(nums[2]))
elif nums[0] == nums[1] / nums[2]:
    print(str(nums[0]) + '=' + str(nums[1]) + '/' + str(nums[2]))
