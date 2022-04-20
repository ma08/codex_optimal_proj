#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Shuailong
# @Email: liangshuailong@gmail.com
# @Date: 2019-05-23 10:45:05
# @Last Modified by: Shuailong
# @Last Modified time: 2019-05-23 10:45:05

import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
print(B // A + (B % A != 0))
