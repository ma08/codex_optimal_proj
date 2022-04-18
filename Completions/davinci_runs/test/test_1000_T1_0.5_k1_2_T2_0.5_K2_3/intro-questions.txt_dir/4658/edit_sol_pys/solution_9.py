class Solution:
    def reverseBits(self, n: int) -> int:
        # n is a binary string of length 32
        bin_str = bin(n)[2:].zfill(32)[::-1]
        return int(bin_str,base=2)
