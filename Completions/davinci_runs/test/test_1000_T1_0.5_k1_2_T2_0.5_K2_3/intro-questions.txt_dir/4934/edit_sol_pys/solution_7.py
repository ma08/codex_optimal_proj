
import sys
import math
import fileinput

for line in fileinput.input():
	h, v = [int(i) for i in line.split()]

print(math.ceil(h/math.sin(math.radians(v))))
