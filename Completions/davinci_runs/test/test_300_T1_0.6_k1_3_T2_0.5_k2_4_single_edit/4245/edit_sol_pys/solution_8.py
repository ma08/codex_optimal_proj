

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print((b+a-1)//a)
