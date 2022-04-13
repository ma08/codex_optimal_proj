
import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a % 9 == 0:
    print(9)
    sys.exit()

if a % 9 == 1:
    print(1)
    sys.exit()

if a % 9 == 2:
    print(2)
    sys.exit()

if a % 9 == 3:
    print(3)
    sys.exit()

if a % 9 == 4:
    print(4)
    sys.exit()

if a % 9 == 5:
    print(5)
    sys.exit()

if a % 9 == 6:
    print(6)
    sys.exit()

if a % 9 == 7:
    print(7)
    sys.exit()

if a % 9 == 8:
    print(8)
    sys.exit()
