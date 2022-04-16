
#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the isValid function below.
def isValid(s):
    if len(s) == 1:
        return "YES"
    dic = {}
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    m = max(dic.values())
    m_key = max(dic, key=dic.get)
    for key in dic:
        if key != m_key:
            if dic[key] == m:
                return "YES"
            else:
                return "NO"
    if m-1 in dic.values():
        return "YES"
    else:
        return "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    fptr.write(result + '\n')
    fptr.close()
