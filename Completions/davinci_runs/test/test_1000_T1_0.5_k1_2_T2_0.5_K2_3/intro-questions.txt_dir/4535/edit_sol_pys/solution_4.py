

class Solution:
    def hammingWeight(self, n: int) -> int:
        n = n & 0xFFFFFFFF
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count

    def hammingWeight_bit_operation(self, n: int) -> int:
        n = n & 0xFFFFFFFF
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight_bin(self, n: int) -> int:
        return bin(n & 0xFFFFFFFF).count("1")
