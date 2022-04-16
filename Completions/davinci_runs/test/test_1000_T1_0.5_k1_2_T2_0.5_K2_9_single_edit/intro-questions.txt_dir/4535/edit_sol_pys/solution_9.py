

class Solution:


s = Solution()
print(s.hammingWeight(11))
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
