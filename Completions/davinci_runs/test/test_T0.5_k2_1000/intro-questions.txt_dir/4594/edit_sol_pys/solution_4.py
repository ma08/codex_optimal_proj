#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

N = int(sys.stdin.readline())
d_list = []
for i in range(N):
    d_list.append(int(sys.stdin.readline()))
d_set = set(d_list)
print(len(d_set))
