

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 11:45:01 2017

@author: antonialarranaga
"""

import numpy as np

def knightlOnAChessboard(n, a, b):
    if a == b:
        return knightlOnAChessboard(n, a, b)
    else:
        return knightlOnAChessboard(n, a, b)
    
n = 5
a = 1
b = 2

    n = int(input())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
