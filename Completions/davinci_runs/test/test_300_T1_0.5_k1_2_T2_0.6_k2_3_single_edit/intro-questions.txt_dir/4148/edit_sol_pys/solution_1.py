import sys
import math

n = int(sys.stdin.readline())
s = sys.stdin.readline()

if n > len(s):
    n = n % len(s)

if n == 0:
    print(s)
else:
    print(s[n:] + s[0:n])
