import math

import sys

def area(a, b, c):
    """
    Given the lengths of the three sides of a triangle, calculate the area.
    """
    s = (a + b + c) / 2
    return math.sqrt(s*(s-a)*(s-b)*(s-c))

inputs = sys.stdin.readline().split()
print(int(area(int(inputs[0]), int(inputs[1]), int(inputs[2]))))
