
import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

sum_of_abc = a + b + c
if sum_of_abc <= 9:
    print(sum_of_abc)
    exit()

if sum_of_abc <= 18:
    print(sum_of_abc - 9)
    exit()

if sum_of_abc <= 27:
    print(sum_of_abc - 18)
    exit()

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
