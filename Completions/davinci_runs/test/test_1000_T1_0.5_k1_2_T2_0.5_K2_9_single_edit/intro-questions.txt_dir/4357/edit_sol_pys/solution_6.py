
import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a + b + c <= 81:
    if a + b + c <= 9:
        print(a + b + c)
        sys.exit()

    if a + b + c <= 18:
        print(a + b + c - 9)
        sys.exit()

    if a + b + c <= 27:
        print(a + b + c - 18)
        sys.exit()

    if a + b + c <= 36:
        print(a + b + c - 27)
        sys.exit()

    if a + b + c <= 45:
        print(a + b + c - 36)
        sys.exit()

    if a + b + c <= 54:
        print(a + b + c - 45)
        sys.exit()

    if a + b + c <= 63:
        print(a + b + c - 54)
        sys.exit()

    if a + b + c <= 72:
        print(a + b + c - 63)
        sys.exit()

if a + b + c <= 81:
    print(a + b + c - 72)
    sys.exit()
