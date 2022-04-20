

import sys

n = int(sys.stdin.readline())

# The base -2 representation of 0 is 0, so just print 0.
if n == 0:
    print("0")

# The base -2 representation of a positive number is the same as the base 2 representation of the negative of that number.
elif n > 0:
    b = bin(n * -1)[2:]
    print(b)

# The base -2 representation of a negative number is the same as the base 2 representation of the negative of that number, with the first digit changed from 0 to 1 and vice versa.
else:
    b = bin(n)[3:]
    print("1" + b)