#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-20 22:00:57
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : level 11 of python challenge
# 
# 思路：这一关没什么难度，只要把不同的字母找出来就可以了，直接拼接成一个字符串
#       然后用set去重就可以了
#
# 备注：1. python challenge home page : http://www.pythonchallenge.com/
#       2. current level url : http://www.pythonchallenge.com/pc/return/5808.html
#       3. next level url : http://www.pythonchallenge.com/pc/return/evil.html
#

s = input()
t = input()

sticky = []
for i in range(len(s)):
    if s[i] != t[i]:
        sticky.append(s[i])

print("".join(set(sticky)))
