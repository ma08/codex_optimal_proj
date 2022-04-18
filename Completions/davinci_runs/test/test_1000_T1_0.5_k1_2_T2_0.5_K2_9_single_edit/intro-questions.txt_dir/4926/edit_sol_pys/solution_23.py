# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:04:32 2019
@author: han-luo
"""

import math

def euler(n = 10):
    return sum(1/math.factorial(i) for i in range(n+1)) 
