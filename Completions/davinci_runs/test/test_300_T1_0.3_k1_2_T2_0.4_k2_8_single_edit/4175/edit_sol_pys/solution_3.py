#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import math
from collections import Counter



def input():
    return sys.stdin.readline()


for i in range(1, n):
    if words[i-1][-1] != words[i][0]:
        print("No")
        sys.exit()

print("Yes")
