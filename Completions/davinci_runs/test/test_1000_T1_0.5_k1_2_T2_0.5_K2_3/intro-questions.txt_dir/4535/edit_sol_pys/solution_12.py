#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 22:21
# @Author  : minp
# @contact : king101125s@gmail.com
# @Site    : 
# @File    : hammingWeight.py
# @Software: PyCharm
class Solution:
    def hammingWeight(self, n: int) -> int:
        n = n & 0xffffffff
        count = 0
        while n > 0:
            n &= n - 1
            count += 1
        return count

    def hammingWeight_bitOperation(self, n: int) -> int:
        n = n & 0xffffffff
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight_bin(self, n: int) -> int:
        return bin(n & 0xffffffff).count("1")
