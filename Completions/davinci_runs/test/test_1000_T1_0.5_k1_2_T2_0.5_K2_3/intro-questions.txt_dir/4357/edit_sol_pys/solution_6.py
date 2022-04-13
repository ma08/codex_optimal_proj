

import sys

inputs = sys.stdin.readline()
a = int(inputs[0]) #1
b = int(inputs[1]) #2
c = int(inputs[2]) #3
d = int(inputs[3]) #4

if a + b + c + d <= 10: #1
    print(a + b + c + d)
    sys.exit()

if a + b + c + d <= 20: #2
    print(a + b + c + d - 10)
    sys.exit()

if a + b + c + d <= 30: #3
    print(a + b + c + d - 20)
    sys.exit()

if a + b + c + d <= 40: #4
    print(a + b + c + d - 30)
    sys.exit()

if a + b + c + d <= 50: #5
    print(a + b + c + d - 40)
    sys.exit()

if a + b + c + d <= 60: #6
    print(a + b + c + d - 50)
    sys.exit()

if a + b + c + d <= 70: #7
    print(a + b + c + d - 60)
    sys.exit()

if a + b + c + d <= 80: #8
    print(a + b + c + d - 70)
    sys.exit()

if a + b + c + d <= 90: #9
    print(a + b + c + d - 80)
    sys.exit()
