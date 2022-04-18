
import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, heapq.heappop(A) * -1)
        return sum(A)
