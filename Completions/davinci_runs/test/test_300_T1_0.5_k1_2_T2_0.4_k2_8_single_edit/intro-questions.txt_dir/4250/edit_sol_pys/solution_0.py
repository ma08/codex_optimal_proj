
#Solution

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = 0
    ar.sort()
    ar.append('#')
    i = 0
    while i<n:
        if ar[i]==ar[i+1]:
            count = count+1
            i+=2
        else:
            i+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

t = s_unique[s_indices[:k]]
print(*t)
