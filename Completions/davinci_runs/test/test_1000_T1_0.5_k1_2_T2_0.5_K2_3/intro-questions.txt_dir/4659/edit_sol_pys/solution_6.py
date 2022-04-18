#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 14:48
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q118_generate.py
# @Note    : https://leetcode-cn.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            tmp = [1]
            for j in range(1, i):
                tmp.append(res[i-1][j-1] + res[i-1][j])
            tmp.append(1)
            res.append(tmp)
        return res
