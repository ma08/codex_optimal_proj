
# test

# def plusOne(digits):
#     """
#     :type digits: List[int]
#     :rtype: List[int]
#     """
#     plus = 1
#     for i in range(len(digits) - 1, -1, -1):
#         if plus == 1:
#             if digits[i] + 1 == 10:
#                 digits[i] = 0
#             else:
#                 digits[i] += 1
#                 plus = 0
#         else:
#             break
#     if plus == 1:
#         digits.insert(0, 1)
#     return digits


# print(plusOne([9, 9, 9]))

# def findMin(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     if len(nums) == 1:
#         return nums[0]
#     if len(nums) == 2:
#         return min(nums[0], nums[1])
#     if nums[0] < nums[len(nums) - 1]:
#         return nums[0]
#     if nums[0] > nums[len(nums) - 1]:
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > nums[mid + 1]:
#                 return nums[mid + 1]
#             if nums[mid] < nums[mid - 1]:
#                 return nums[mid]
#             if nums[mid] > nums[0]:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return nums[0]


# print(findMin([4, 5, 6, 7, 0, 1, 2]))


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if target < nums[0]:
        return 0
    if target > nums[len(nums) - 1]:
        return len(nums)
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


print(searchInsert([1, 3, 5, 6], 5))
