#!/bin/python3


import math
import os
import random
import re
import sys



# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                num1 = str(ar[i]) + str(ar[j])
                num1 = int(num1)
                if num1 % k == 0:
                    res += 1

    return res


n, k = map(int, input().split())
a = list(map(int, input().split()))

result = divisibleSumPairs(n, k, a)
print(result)
