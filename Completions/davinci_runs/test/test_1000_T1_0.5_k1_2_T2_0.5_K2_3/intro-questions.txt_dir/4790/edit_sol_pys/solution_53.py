
#!/bin/python3

import sys

def solve(n):
    count = 0
    for i in range(len(n)):
        if n[i] == 'B':
            count += 1
    if count == len(n) or count == 0:
        return 0
    else:
        return 1

n = input().strip()
result = solve(n)
print(result)
