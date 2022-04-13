import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)  # O(N)

# time complexity: O(N + KlogN)
        for _ in range(K):
            num = heapq.heappop(A) * -1  # O(logN)
            heapq.heappush(A, num)
        return sum(A)
