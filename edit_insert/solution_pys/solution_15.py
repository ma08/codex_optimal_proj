

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # if not nums:
        #     return -1
            
        # left = 0
        # right = len(nums) - 1
            
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if nums[mid] == target:
        #         return mid
                
        #     if nums[mid] >= nums[left]:
        #         if target >= nums[left] and target < nums[mid]:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     else:
        #         if target > nums[mid] and target <= nums[right]:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
                
        # return -1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if nums[0] == target:
                return 1
            else:
                return 0
        if len(nums) == 2:
            if nums[0] == target:
                return 1
            elif nums[1] == target:
                return 1
                else:
                return 0
        mid = len(nums) // 2
        if nums[mid] == target:
            return 1
        elif nums[mid] > target:
            return self.search(nums[:mid], target)
        elif nums[mid] < target:
            return self.search(nums[mid+1:], target)
