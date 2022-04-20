
#!/usr/bin/python3
import math
import os
import random
import re
import sys
 
# Complete the repeatedString function below.
def repeatedString(s, n):
    total = 0
    for i in s:
        if i == 'a':
            total += 1
    total *= n // len(s)
    for i in s[:n % len(s)]:
        if i == 'a':
            total += 1
    return total
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    s = input()
 
    n = int(input())
 
    result = repeatedString(s, n)
 
    fptr.write(str(result) + '\n')
 
    fptr.close()
