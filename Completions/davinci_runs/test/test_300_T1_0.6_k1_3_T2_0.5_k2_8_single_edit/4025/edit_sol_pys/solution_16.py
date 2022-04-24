import sys
import math

a, b, c = raw_input().split()

print(int(a) + int(b) + int(c) - max(int(a), int(b), int(c)) - min(int(a), int(b), int(c)))
