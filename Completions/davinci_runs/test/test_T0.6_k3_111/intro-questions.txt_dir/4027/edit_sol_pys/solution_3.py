#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 9:39
# @Author  : ZJJ
# @Email   : 597105373@qq.com

import sys
import math

def minDiff(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 1 

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    print(minDiff(n))
