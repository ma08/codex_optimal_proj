

import sys, math

inputs = sys.stdin.readline()
a = int(inputs.split()[0])
b = int(inputs.split()[1])
c = int(inputs.split()[2])

n = a + b + c

if n <= 9:
    print(n)
    sys.exit()

if n <= 18:
    print(n - 9)
    sys.exit()

if n <= 27:
    print(n - 18)
    sys.exit()

if n <= 36:
    print(n - 27)
    sys.exit()

if n <= 45:
    print(n - 36)
    sys.exit()

if n <= 54:
    print(n - 45)
    sys.exit()

if n <= 63:
    print(n - 54)
    sys.exit()

if n <= 72:
    print(n - 63)
    sys.exit()

if n <= 81:
    print(n - 72)
    sys.exit()
