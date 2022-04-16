

class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        count = 0
        for num in A:
            cur += num
            if cur == target:
                count += 1
                cur = 0


if __name__ == '__main__':
    s = Solution()
    assert s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]) == True
    assert s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]) == False
    assert s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]) == True
        return count == 3
