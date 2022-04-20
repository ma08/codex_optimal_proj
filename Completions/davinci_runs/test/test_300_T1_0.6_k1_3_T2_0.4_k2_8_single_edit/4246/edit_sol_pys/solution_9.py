#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14
# @Author  : Edrain

S = input()
T = input()
ans = 0
for i in range(3):
    if S[i] == T[i]:
        ans += 1
print(ans)
