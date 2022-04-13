class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        maxSum = float('-inf')
        currentSum = 0
        for num in nums:
            currentSum += num
            maxSum = max(maxSum, currentSum)
            currentSum = max(currentSum, 0)
        return maxSum

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         if not nums:
#             return None
#         maxSum = float('-inf')
#         currentSum = 0
#         for num in nums:
#             currentSum += num
#             maxSum = max(maxSum, currentSum)
#             currentSum = max(currentSum, 0)
#         return maxSum
