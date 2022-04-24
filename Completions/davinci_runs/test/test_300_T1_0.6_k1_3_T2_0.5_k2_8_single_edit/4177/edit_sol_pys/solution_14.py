# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:20:04 2020
@author: krishna
"""

s = input()

for i in range(len(s)):
    s = s[:i] + "x" + s[i+1:] 
print(s)
