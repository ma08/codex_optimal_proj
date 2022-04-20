

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY s
#

n = int(input())
s = []

for _ in range(n):
    s_item = input()
    s.append(s_item)

print(solve(n, s))
