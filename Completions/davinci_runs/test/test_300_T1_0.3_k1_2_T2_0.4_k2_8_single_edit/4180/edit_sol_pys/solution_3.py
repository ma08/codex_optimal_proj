

import sys

n = int(sys.stdin.readline())

print(1000 - n % 1000 if n % 1000 != 0 else 0)
