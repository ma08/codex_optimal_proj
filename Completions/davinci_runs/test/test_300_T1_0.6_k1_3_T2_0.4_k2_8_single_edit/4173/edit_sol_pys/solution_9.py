
#!/bin/python
#
# HackerRank
# Algorithms: Implementation
#
import sys, re
from collections import Counter
#
# Complete the function below.
#
def isValid(s):
    #
    # Write your code here.
    #
    cnt = Counter(s)
    cnt = cnt.values()
    m = min(cnt)
    cnt = Counter(cnt)
    if len(cnt) == 1:
        return "YES"
    elif len(cnt) == 2:
        if m in cnt.keys() and 1 in cnt.values():
            return "YES"
        elif m + 1 in cnt.keys() and 1 in cnt.values():
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
#
s = raw_input().strip()
result = isValid(s)
print(result)
