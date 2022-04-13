

class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:]
        n = n.zfill(32)  # zfill() 函数返回指定长度的字符串，原字符串右对齐，前面填充0.
        n = n[::-1]
        return int(n, 2)
