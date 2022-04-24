from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2
        return nums[n // 2]


if __name__ == "__main__":
    s = Solution()
    answer = s.findMedianSortedArrays([1, 3], [2])
    print(answer)
