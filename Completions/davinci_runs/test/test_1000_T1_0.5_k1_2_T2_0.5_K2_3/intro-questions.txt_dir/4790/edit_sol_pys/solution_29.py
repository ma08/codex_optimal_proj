
#!/bin/python3

import sys

def solve(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'B':
            count += 1
    if count == len(s) or count == 0:
        return 0
    else:
        return 1

s = input().strip()
result = solve(s)
print(result)
