

s = list(input())

n = len(s)

odds = [s[i] for i in range(n) if i % 2 == 0]
evens = [s[i] for i in range(n) if i % 2 == 1]

if all(x in ['R', 'U', 'D'] for x in odds) and all(x in ['L', 'U', 'D'] for x in evens):
    print("Yes")
else:
    print("No")

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append('#')
    i = 0
    ans = 0
    while i<n:
        if ar[i]==ar[i+1]:
            ans+=1
            i+=2
        else:
            i+=1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
