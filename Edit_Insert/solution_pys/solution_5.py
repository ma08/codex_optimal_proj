#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # left part is ascending
            if nums[mid] >= nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right part is ascending
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))
