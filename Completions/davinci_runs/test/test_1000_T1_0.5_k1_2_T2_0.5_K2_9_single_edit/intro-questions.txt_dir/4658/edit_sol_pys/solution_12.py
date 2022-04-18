# @file: ReverseBits.py
# @author: Daniel Yuan
# @brief:
# @date: 2019-07-22

class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.zfill(32)
        n = n[::-1]
        return int(n, 2)
