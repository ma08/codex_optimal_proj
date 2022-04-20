

# Version 1 

def solution(nums):
    # Your code here 
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == i:
            continue
        else:
            return i
    return len(nums)

# Version 2

def solution(nums):
    # Your code here 
    nums.sort()
    for i in range(len(nums)):
        if nums[i] == i:
            continue
        else:
            return i
    return len(nums)
