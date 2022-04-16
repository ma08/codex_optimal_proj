

#!/bin/python3

import sys

def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'B':
            count += 1
    return count
    
s = input().strip()
result = solve(s)
print(result)
