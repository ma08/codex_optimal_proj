import heapq


class Solution:
    def largestSumAfterKNegations(self, A, K):
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, heapq.heappop(A) * -1)
        return sum(A)
