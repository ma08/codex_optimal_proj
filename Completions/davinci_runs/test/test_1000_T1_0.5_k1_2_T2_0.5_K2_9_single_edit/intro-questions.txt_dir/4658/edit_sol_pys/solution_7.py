

class Solution:
    def reverseBits(self, n: int) -> int:
        print(n)
        n = bin(n)[2:]
        print(n)
        n = n.zfill(32)
        n = n[::-1]
        return int(n, 2)
