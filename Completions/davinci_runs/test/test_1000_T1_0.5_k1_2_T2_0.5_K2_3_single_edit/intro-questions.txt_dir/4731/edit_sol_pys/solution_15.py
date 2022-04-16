#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:17:47 2019
@author: Aman
"""

n = int(input())
words = []
for i in range(n):
    words.append(input().lower())

player = 1
for i in range(n - 1):
    if words[i][-1] != words[i + 1][0]:
        print("Player {} lost".format(player))
        break
    if i < n - 2 and words[i + 1] == words[i + 2]:
        print("Player {} lost".format(player))
        break
    player = (player % 2) + 1
else:
    print("Fair Game")
