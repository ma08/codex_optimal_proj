#!/usr/bin/env python
# coding: utf-8
# Author: Olga Romanenko
# Created: 02.12.2018

import math

a, b = map(int, input().split())

for i in range(1, a+1):
    if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
        print(i)
        exit()
print(-1)
