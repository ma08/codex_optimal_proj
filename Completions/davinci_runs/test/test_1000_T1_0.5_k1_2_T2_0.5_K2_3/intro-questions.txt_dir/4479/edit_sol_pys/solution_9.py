import heapq


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        for _ in range(K):
            heapq.heappush(A, heapq.heappop(A) * -1)


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for i in range(len(A)):
            if A[i] < 0 and K > 0:
                A[i] = -A[i]
                K -= 1
            elif A[i] > 0 and K % 2 != 0:
                A[i] = -A[i]
                break
        return sum(A)
        return sum(A)
