

# Version 1

def solution(n):
    # Your code here
    nums = list(str(n))
    while len(nums) > 1:
        next_sum = 0
        for num in nums:
            next_sum += int(num) ** 2
        nums = list(str(next_sum))
    return nums[0]

# Version 2

def solution(n):
    # Your code here
    nums = list(str(n))
    while len(nums) > 1:
        next_sum = 0
        for num in nums:
            next_sum += int(num) ** 2
        nums = list(str(next_sum))
    return nums[0]
