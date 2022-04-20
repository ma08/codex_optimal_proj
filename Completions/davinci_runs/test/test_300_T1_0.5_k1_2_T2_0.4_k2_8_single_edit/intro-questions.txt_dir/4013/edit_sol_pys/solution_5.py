
#!/bin/python3
import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    curr_min = min(arr)
    curr_max = max(arr)
    print(curr_max - curr_min - 2*min(curr_max - curr_min, min(arr.count(curr_min), arr.count(curr_max))))
