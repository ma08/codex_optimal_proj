
import math

a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
elif b >= a and b >= c:
    if a >= c:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
else:
    if a >= b:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))  # Heron's formula
