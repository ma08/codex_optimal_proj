

import sys

a, b = map(int, sys.stdin.readline().split())
print(int(a / b) + (1 if a % b > 0 else 0))
