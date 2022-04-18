

class Solution:
    def hammingWeight(self, n: int) -> int:


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return bin(n).count('1')
