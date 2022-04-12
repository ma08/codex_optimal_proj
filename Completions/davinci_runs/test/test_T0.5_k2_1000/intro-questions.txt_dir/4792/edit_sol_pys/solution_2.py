
def remove_adjacent(nums):
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]:
            nums = nums[:i] + nums[i+1:]
            i -= 1
    return nums

print(remove_adjacent([1, 2, 2, 3]))
