#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 14:21
# @Author  : Durat
# @Email   : durant.zeng@sunvalley.com.cn
# @File    : generate.py
# @Software: PyCharm
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
