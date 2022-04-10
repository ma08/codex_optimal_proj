

import sys

# read data for n sequences
n, k = map(int, sys.stdin.readline().rstrip().split())

# read the nth sequence
s = sys.stdin.readline().rstrip()

# print output
print(n - k)