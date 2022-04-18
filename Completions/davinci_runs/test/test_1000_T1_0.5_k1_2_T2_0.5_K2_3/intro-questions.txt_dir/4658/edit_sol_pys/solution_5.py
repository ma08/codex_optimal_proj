class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]  # 0b1001000100001111110011100101111
        n = n.zfill(32)  # 001001000100001111110011100101111
        n = n[::-1]  # 11101001011000011110011000100110
        return int(n, 2)  # 964176192
