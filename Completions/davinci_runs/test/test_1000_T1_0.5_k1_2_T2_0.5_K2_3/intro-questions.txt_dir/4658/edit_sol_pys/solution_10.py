class Solution:
    def reverseBits(self, n: int) -> int:
        # n is a binary string of length 32 
        bin_str = bin(n)[2:]
        bin_str = bin_str.zfill(32)
        bin_str = bin_str[::-1]
        return int(bin_str, 2)
