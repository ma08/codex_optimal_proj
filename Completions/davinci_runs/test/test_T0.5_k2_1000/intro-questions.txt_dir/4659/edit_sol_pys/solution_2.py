#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 20:59
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q118_generate.py
# @Note    : https://leetcode-cn.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    res[i].append(1)
                else:

                    res[i].append(res[i-1][j-1] + res[i-1][j])
        return res
