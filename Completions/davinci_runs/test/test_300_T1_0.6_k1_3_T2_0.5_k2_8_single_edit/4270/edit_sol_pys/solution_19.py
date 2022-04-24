def median(nums):
    nums.sort()
    if len(nums) % 2 == 0:
        return (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2 - 1)]) / 2
    else:
        return nums[int(len(nums) / 2)]
