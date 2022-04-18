'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u,v) which consists of one element from the first array and one element from the second array.
Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Use heap to store the smallest sum
        if not nums1 or not nums2:
            return []
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                sum_ = nums1[i] + nums2[j]
                if len(heap) < k:
                    heapq.heappush(heap, (-sum_, i, j))
                else:
                    if sum_ < -heap[0][0]:
                        heapq.heappushpop(heap, (-sum_, i, j))
                    else:
                        break
        res = []
        while heap:
            sum, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
        return res[::-1]
