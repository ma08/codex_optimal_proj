#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 20:59
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q118_generate.py
# @Note    : https://leetcode-cn.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        res = [1, 1]
        for i in range(2, rowIndex+1):
            res.append(1)
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j-1]
        return res[:rowIndex+1]
