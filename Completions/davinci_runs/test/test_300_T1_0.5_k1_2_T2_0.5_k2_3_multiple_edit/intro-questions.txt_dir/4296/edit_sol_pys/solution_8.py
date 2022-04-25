

import sys

n = int(input())

if n % 3 == 0:
    print(n // 3)
    sys.exit()

if n % 3 == 1:
    print((n-10) // 3 + 1)
    sys.exit()

if n % 3 == 2:
    print((n-5) // 3 + 1)
    sys.exit()
