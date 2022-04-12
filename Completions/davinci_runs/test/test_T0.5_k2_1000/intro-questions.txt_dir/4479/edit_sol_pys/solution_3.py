class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        for _ in range(K):
            A[0] = -A[0]
            A.sort()
        return sum(A)
