

import sys
import re
n = int(input())
for i in range(n):
    a = input()
    if re.match(r'^[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z0-9_]+$', a):
        print('YES')
    else:
        print('NO')
