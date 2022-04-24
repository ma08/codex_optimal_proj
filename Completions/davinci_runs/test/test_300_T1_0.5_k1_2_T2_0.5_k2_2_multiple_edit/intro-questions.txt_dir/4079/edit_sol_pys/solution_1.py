#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 10:40
# @Author  : cai
# @contact : yuwei.chen@yunzhenxin.com
# @File    : Q26_isLongPressedName.py
# @Note    : https://leetcode-cn.com/problems/long-pressed-name/



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return True
