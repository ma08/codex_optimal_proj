

class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.zfill(32)
        n = n[::-1]
        return int(n, 2)
