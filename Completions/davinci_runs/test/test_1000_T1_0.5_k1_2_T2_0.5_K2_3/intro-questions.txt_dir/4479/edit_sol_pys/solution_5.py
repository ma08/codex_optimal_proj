import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)  # O(N)  

# time complexity: O(N + KlogN)
        for _ in range(K):
            heapq.heappush(A, heapq.heappop(A) * -1)  # O(logN)
        return sum(A)
