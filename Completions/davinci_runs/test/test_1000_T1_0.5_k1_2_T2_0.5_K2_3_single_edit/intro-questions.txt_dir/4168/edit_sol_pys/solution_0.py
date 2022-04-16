

import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

if n > 0:
    print(bin(n)[2:])
    exit()

# n < 0
print(bin(n)[3:])
