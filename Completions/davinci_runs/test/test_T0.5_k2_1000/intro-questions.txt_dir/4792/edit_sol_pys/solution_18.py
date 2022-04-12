
def remove_adjacent(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i)
        else:
            i += 1
    return nums

print(remove_adjacent([1,2,2,3,4,4,4,4,5]))
