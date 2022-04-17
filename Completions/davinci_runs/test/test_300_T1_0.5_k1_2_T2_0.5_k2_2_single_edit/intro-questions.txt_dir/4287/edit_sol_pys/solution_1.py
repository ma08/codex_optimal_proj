#-----Description-----
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

#-----Solution-----
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)


print(singleNumber([2,2,1]))
print(singleNumber([4,1,2,1,2]))
#-----Test-----
