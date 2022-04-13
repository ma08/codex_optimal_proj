

#!/bin/python3

import sys

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))

tallest = max(height)
if tallest > k:
    print(tallest - k)
else:
    print(0)
