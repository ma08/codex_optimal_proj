
import sys

inputs = sys.stdin.readline().split()
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])

if a + b + c <= 81:
    print(a + b + c) 
elif a + b + c <= 90:
    print(a + b + c - 9)
elif a + b + c <= 99:
    print(a + b + c - 18)
elif a + b + c <= 108:
    print(a + b + c - 27)
elif a + b + c <= 117:
    print(a + b + c - 36)
elif a + b + c <= 126:
    print(a + b + c - 45)
elif a + b + c <= 135:
    print(a + b + c - 54)
elif a + b + c <= 144:
    print(a + b + c - 63)
elif a + b + c <= 153:
    print(a + b + c - 72)
