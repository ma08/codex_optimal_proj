#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 12:55:06 2019

@author: bijayamanandhar
"""


n = int(input())
s = input()

# check if the sequence is already regular
def is_regular(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True

# count the number of open and close brackets
def count_brackets(s):
    open_ = 0
    close_ = 0
    for char in s:
        if char == '(':
            open_ += 1
        else:
            close_ += 1
    return open_, close_

def count_changes(s):
    if is_regular(s):
        return 0
    open_, close_ = count_brackets(s)
    if open_ == close_:
        return 0
    return open_ + close_ - abs(open_ - close_)

print(count_changes(s))
