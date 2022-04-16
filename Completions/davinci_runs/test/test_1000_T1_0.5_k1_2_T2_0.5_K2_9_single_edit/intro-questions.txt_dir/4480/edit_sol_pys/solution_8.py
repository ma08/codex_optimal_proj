#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 下午3:03
# @Author  : Aries
# @Site    : 
# @File    : file.py
# @Software: PyCharm

class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        total = sum(A)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        count = 0
        for num in A:
            cur += num
            if cur == target:
                count += 1
                cur = 0
        return count == 3
