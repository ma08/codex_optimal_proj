

import sys
import math

x = float(raw_input())

s = str(x)

s = s.split('.')

integer_part = int(s[0])

decimal_part = int(s[1])

a = 0
b = 0

for i in range(1,11):
	for j in range(1,11):
		if (i * integer_part + j * decimal_part) == int(math.pow(10,6)):
			a = i
			b = j
			break
	
print str(a) + " " + str(b)