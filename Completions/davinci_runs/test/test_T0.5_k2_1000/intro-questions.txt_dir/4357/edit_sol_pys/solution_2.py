

import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a + b + c <= 9: # 1
    print(a + b + c)
    sys.exit()

if a + b + c <= 18: # 2
    print(a + b + c - 9)
    sys.exit()

if a + b + c <= 27: # 3
    print(a + b + c - 18)
    sys.exit()

if a + b + c <= 36: # 4
    print(a + b + c - 27)
    sys.exit()

if a + b + c <= 45: # 5
    print(a + b + c - 36)
    sys.exit()

if a + b + c <= 54: # 6
    print(a + b + c - 45)
    sys.exit()

if a + b + c <= 63: # 7
    print(a + b + c - 54)
    sys.exit()

if a + b + c <= 72: # 8
    print(a + b + c - 63)
    sys.exit()

if a + b + c <= 81: # 9
    print(a + b + c - 72)
    sys.exit()

if a + b + c <= 90: # 10
    print(a + b + c - 81)
    sys.exit()
